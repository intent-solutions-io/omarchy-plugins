(() => {
  "use strict";

  const grid = document.querySelector("#plugin-grid");
  const resultStatus = document.querySelector("#result-status");
  const search = document.querySelector("#plugin-search");
  const familyFilters = document.querySelector("#family-filters");
  const statusFilters = document.querySelector("#status-filters");
  const toast = document.querySelector("#toast");

  const lifecycleOrder = ["listed", "under-review", "developing", "unreleased", "not-listed", "retired"];
  const lifecycleLabels = {
    listed: "Listed",
    "under-review": "In review",
    developing: "Developing",
    unreleased: "Unreleased",
    "not-listed": "Not listed",
    retired: "Retired",
  };
  const allowedLifecycles = new Set(lifecycleOrder);
  const allowedExternalHosts = new Set(["github.com", "plugins.omarchy.org", "raw.githubusercontent.com"]);

  const state = {
    plugins: [],
    status: "all",
    family: "all",
    query: "",
    loadState: "loading",
  };

  function escapeHtml(value) {
    return String(value ?? "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  function compactNumber(value) {
    return new Intl.NumberFormat("en-US", { notation: "compact", maximumFractionDigits: 1 }).format(value || 0);
  }

  function safeExternalUrl(value) {
    try {
      const url = new URL(String(value || ""));
      if (url.protocol !== "https:" || !allowedExternalHosts.has(url.hostname)) return "";
      return url.href;
    } catch {
      return "";
    }
  }

  function isoDay(value) {
    const date = new Date(value);
    if (Number.isNaN(date.getTime())) return "unknown";
    return new Intl.DateTimeFormat("en-US", {
      year: "numeric",
      month: "short",
      day: "numeric",
      timeZone: "UTC",
    }).format(date);
  }

  function showToast(message) {
    toast.textContent = message;
    toast.classList.add("visible");
    window.clearTimeout(showToast.timer);
    showToast.timer = window.setTimeout(() => toast.classList.remove("visible"), 2200);
  }

  function assertPlugin(plugin, index) {
    const requiredStrings = ["id", "name", "slug", "repoUrl", "pitch", "family", "lifecycle"];
    for (const key of requiredStrings) {
      if (typeof plugin?.[key] !== "string" || !plugin[key].trim()) {
        throw new Error(`Plugin ${index + 1} has invalid ${key}`);
      }
    }
    if (!allowedLifecycles.has(plugin.lifecycle)) throw new Error(`Plugin ${plugin.id} has invalid lifecycle`);
    if (!safeExternalUrl(plugin.repoUrl)) throw new Error(`Plugin ${plugin.id} has invalid repository URL`);
    if (!plugin.github || !Number.isInteger(plugin.github.stars) || plugin.github.stars < 0) {
      throw new Error(`Plugin ${plugin.id} has invalid GitHub metadata`);
    }
    if (!plugin.preview || typeof plugin.preview.status !== "string") {
      throw new Error(`Plugin ${plugin.id} has invalid preview metadata`);
    }
    if (!plugin.manifest || typeof plugin.manifest.status !== "string") {
      throw new Error(`Plugin ${plugin.id} has invalid manifest metadata`);
    }
  }

  function marketplaceAction(plugin) {
    const marketplaceUrl = safeExternalUrl(plugin.marketplaceUrl);
    const submissionUrl = safeExternalUrl(plugin.submissionUrl);
    if (marketplaceUrl) {
      return `<a href="${escapeHtml(marketplaceUrl)}" target="_blank" rel="noreferrer">Marketplace</a>`;
    }
    if (submissionUrl) {
      return `<a href="${escapeHtml(submissionUrl)}" target="_blank" rel="noreferrer">Review record</a>`;
    }
    return "";
  }

  function previewMarkup(plugin) {
    const previewUrl = safeExternalUrl(plugin.preview?.url || plugin.previewUrl);
    if (plugin.preview?.status !== "verified" || !previewUrl) {
      return `<div class="card-preview image-missing" role="img" aria-label="No verified preview is currently available for ${escapeHtml(plugin.name)}"><span>Preview unavailable</span></div>`;
    }
    return `<div class="card-preview"><img src="${escapeHtml(previewUrl)}" alt="${escapeHtml(plugin.name)} plugin interface preview" width="1280" height="720" loading="lazy"></div>`;
  }

  function sourceFacts(plugin) {
    const manifestStatus = String(plugin.manifest?.status || "unknown").replaceAll("-", " ");
    return `<dl class="source-facts" aria-label="Repository health">
      <div><dt>Stars</dt><dd>${compactNumber(plugin.github?.stars)}</dd></div>
      <div><dt>Updated</dt><dd>${escapeHtml(isoDay(plugin.github?.pushedAt))}</dd></div>
      <div><dt>Manifest</dt><dd class="manifest-${escapeHtml(plugin.manifest?.status)}">${escapeHtml(manifestStatus)}</dd></div>
    </dl>`;
  }

  function metricsRow(plugin) {
    if (!plugin.metrics) {
      return `<div class="metrics"><span>${escapeHtml(lifecycleLabels[plugin.lifecycle] || "Marketplace status unavailable")}</span></div>`;
    }
    return `<div class="metrics" aria-label="Marketplace engagement">
      <span><strong>${compactNumber(plugin.metrics.views)}</strong> views</span>
      <span><strong>${compactNumber(plugin.metrics.copies)}</strong> copies</span>
      <span><strong>${compactNumber(plugin.metrics.hearts)}</strong> hearts</span>
    </div>`;
  }

  function pluginCard(plugin) {
    const lifecycleLabel = lifecycleLabels[plugin.lifecycle] || plugin.lifecycle;
    const copyButton = plugin.installCommand
      ? `<button type="button" data-copy-install="${escapeHtml(plugin.id)}">Copy install</button>`
      : "";
    return `<article class="plugin-card lifecycle-${escapeHtml(plugin.lifecycle)}" data-plugin-id="${escapeHtml(plugin.id)}">
      ${previewMarkup(plugin)}
      <div class="card-body">
        <div class="card-meta">
          <span class="status-badge ${escapeHtml(plugin.lifecycle)}">${escapeHtml(lifecycleLabel)}</span>
          <span class="category-label">${escapeHtml(plugin.category)}</span>
        </div>
        <p class="family-label">${escapeHtml(plugin.family)}</p>
        <h3>${escapeHtml(plugin.name)}</h3>
        <p class="pitch">${escapeHtml(plugin.pitch)}</p>
        ${sourceFacts(plugin)}
        ${metricsRow(plugin)}
        <div class="card-actions">
          <a href="plugins/${encodeURIComponent(plugin.slug)}/">Details</a>
          ${marketplaceAction(plugin)}
          <a href="${escapeHtml(safeExternalUrl(plugin.repoUrl))}" target="_blank" rel="noreferrer">GitHub</a>
          ${copyButton}
        </div>
      </div>
    </article>`;
  }

  function filteredPlugins() {
    const query = state.query.trim().toLowerCase();
    return state.plugins.filter((plugin) => {
      const matchesStatus = state.status === "all" || plugin.lifecycle === state.status;
      const matchesFamily = state.family === "all" || plugin.family === state.family;
      const haystack = [plugin.name, plugin.pitch, plugin.category, plugin.family, plugin.lifecycle, ...(plugin.tags || [])].join(" ").toLowerCase();
      return matchesStatus && matchesFamily && (!query || haystack.includes(query));
    });
  }

  function wireCards() {
    grid.querySelectorAll("img").forEach((image) => {
      image.addEventListener("error", () => {
        image.hidden = true;
        image.parentElement.classList.add("image-missing");
        image.parentElement.insertAdjacentHTML("beforeend", "<span>Preview unavailable</span>");
      }, { once: true });
    });

    grid.querySelectorAll("[data-copy-install]").forEach((button) => {
      button.addEventListener("click", async () => {
        const plugin = state.plugins.find((entry) => entry.id === button.dataset.copyInstall);
        if (!plugin?.installCommand) return;
        try {
          await navigator.clipboard.writeText(plugin.installCommand);
          showToast(`${plugin.name} install command copied`);
        } catch {
          showToast("Copy failed. Open the marketplace listing for the command.");
        }
      });
    });
  }

  function render() {
    if (state.loadState === "failed") return;
    const visible = filteredPlugins();
    grid.innerHTML = visible.length
      ? visible.map(pluginCard).join("")
      : '<div class="empty-state"><h3>No plugins match those filters.</h3><p>Clear a filter or try a broader search.</p></div>';
    resultStatus.textContent = `Showing ${visible.length} of ${state.plugins.length} plugins`;
    wireCards();
  }

  function setPressed(container, dataKey, selected) {
    container.querySelectorAll(`[data-${dataKey}]`).forEach((button) => {
      const active = button.dataset[dataKey] === selected;
      button.classList.toggle("active", active);
      button.setAttribute("aria-pressed", String(active));
    });
  }

  function buildStatusFilters(plugins) {
    const present = new Set(plugins.map((plugin) => plugin.lifecycle));
    const statuses = lifecycleOrder.filter((status) => present.has(status));
    statusFilters.innerHTML = ["all", ...statuses].map((status) => {
      const label = status === "all" ? "All statuses" : lifecycleLabels[status];
      return `<button class="filter${status === "all" ? " active" : ""}" type="button" data-status="${escapeHtml(status)}" aria-pressed="${status === "all"}">${escapeHtml(label)}</button>`;
    }).join("");
  }

  function buildFamilyFilters(plugins, configuredFamilies) {
    const present = new Set(plugins.map((plugin) => plugin.family));
    const ordered = Array.isArray(configuredFamilies)
      ? configuredFamilies.map((family) => typeof family === "string" ? family : family?.name).filter((family) => present.has(family))
      : [];
    const families = [...ordered, ...[...present].filter((family) => !ordered.includes(family)).sort()];
    familyFilters.innerHTML = ["all", ...families].map((family) => {
      const label = family === "all" ? "Every family" : family;
      return `<button class="family-filter${family === "all" ? " active" : ""}" type="button" data-family="${escapeHtml(family)}" aria-pressed="${family === "all"}">${escapeHtml(label)}</button>`;
    }).join("");
  }

  function formatFreshness(value) {
    const date = new Date(value);
    if (Number.isNaN(date.getTime())) return "current catalogue snapshot";
    return new Intl.DateTimeFormat("en-US", { year: "numeric", month: "short", day: "numeric", timeZone: "UTC" }).format(date) + " UTC";
  }

  function updatePortfolioFacts(data) {
    const plugins = data.plugins;
    const listed = plugins.filter((plugin) => plugin.lifecycle === "listed").length;
    const roadmap = plugins.filter((plugin) => !["listed", "retired"].includes(plugin.lifecycle)).length;
    const stars = plugins.reduce((sum, plugin) => sum + plugin.github.stars, 0);
    const previews = plugins.filter((plugin) => plugin.preview.status === "verified").length;
    const aligned = plugins.filter((plugin) => plugin.manifest.status === "aligned").length;
    document.querySelector("#listed-count").textContent = listed;
    document.querySelector("#roadmap-count").textContent = roadmap;
    document.querySelector("#repo-count").textContent = plugins.length;
    document.querySelector("#star-count").textContent = stars;
    document.querySelector("#ledger-listed").textContent = `${listed} / ${plugins.length}`;
    document.querySelector("#ledger-previews").textContent = `${previews} / ${plugins.length}`;
    document.querySelector("#ledger-manifests").textContent = `${aligned} / ${plugins.length}`;
    document.querySelector("#catalog-summary").textContent = `${listed} official listings, ${roadmap} on the public roadmap, and ${stars} GitHub stars across the collection.`;
    document.querySelector("#source-health-summary").innerHTML = `<strong>Source health:</strong> ${aligned} aligned manifests and ${previews} verified repository previews.`;
  }

  async function loadCatalog() {
    try {
      const response = await fetch("data/plugins.json", { cache: "no-store" });
      if (!response.ok) throw new Error(`Catalogue request failed: ${response.status}`);
      const data = await response.json();
      if (!Array.isArray(data.plugins) || data.plugins.length === 0) throw new Error("Catalogue does not contain plugins");
      data.plugins.forEach(assertPlugin);

      state.plugins = data.plugins;
      state.loadState = "ready";
      updatePortfolioFacts(data);
      document.querySelector("#data-freshness").textContent = formatFreshness(data.generatedAt);
      const marketplaceAuthorUrl = safeExternalUrl(data.publisher?.marketplaceUrl);
      const templateUrl = safeExternalUrl(data.template?.repoUrl);
      if (marketplaceAuthorUrl) document.querySelector("#marketplace-author-link").href = marketplaceAuthorUrl;
      if (templateUrl) document.querySelector("#template-link").href = templateUrl;
      if (typeof data.template?.pitch === "string") document.querySelector("#template-pitch").textContent = data.template.pitch;

      buildStatusFilters(data.plugins);
      buildFamilyFilters(data.plugins, data.families);
      grid.setAttribute("aria-busy", "false");
      render();
    } catch (error) {
      state.loadState = "failed";
      grid.setAttribute("aria-busy", "false");
      const empty = document.createElement("div");
      empty.className = "empty-state";
      const heading = document.createElement("h3");
      heading.textContent = "The catalogue could not load.";
      const detail = document.createElement("p");
      detail.textContent = error instanceof Error ? error.message : "Unknown catalogue error";
      const repositoryLink = document.createElement("a");
      repositoryLink.href = "https://github.com/intent-solutions-io/omarchy-plugins";
      repositoryLink.textContent = "Open the repository catalogue";
      empty.append(heading, detail, repositoryLink);
      grid.replaceChildren(empty);
      resultStatus.textContent = "Catalogue unavailable";
    }
  }

  statusFilters.addEventListener("click", (event) => {
    const button = event.target.closest("[data-status]");
    if (!button) return;
    state.status = button.dataset.status;
    setPressed(statusFilters, "status", state.status);
    render();
  });

  familyFilters.addEventListener("click", (event) => {
    const button = event.target.closest("[data-family]");
    if (!button) return;
    state.family = button.dataset.family;
    setPressed(familyFilters, "family", state.family);
    render();
  });

  search.addEventListener("input", () => {
    state.query = search.value;
    render();
  });

  document.addEventListener("keydown", (event) => {
    const typing = ["INPUT", "TEXTAREA", "SELECT"].includes(document.activeElement?.tagName);
    if (event.key === "/" && !typing) {
      event.preventDefault();
      search.focus();
    }
    if (event.key === "Escape" && document.activeElement === search) {
      search.value = "";
      state.query = "";
      search.blur();
      render();
    }
  });

  loadCatalog();
})();
