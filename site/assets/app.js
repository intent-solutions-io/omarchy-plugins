(() => {
  "use strict";

  const grid = document.querySelector("#plugin-grid");
  const resultStatus = document.querySelector("#result-status");
  const search = document.querySelector("#plugin-search");
  const categoryFilters = document.querySelector("#category-filters");
  const statusFilters = document.querySelector("#status-filters");
  const toast = document.querySelector("#toast");

  const state = {
    plugins: [],
    status: "all",
    category: "all",
    query: "",
    loadState: "loading",
  };

  const allowedExternalHosts = new Set([
    "github.com",
    "plugins.omarchy.org",
    "raw.githubusercontent.com",
  ]);

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

  function showToast(message) {
    toast.textContent = message;
    toast.classList.add("visible");
    window.clearTimeout(showToast.timer);
    showToast.timer = window.setTimeout(() => toast.classList.remove("visible"), 2200);
  }

  function marketplaceAction(plugin) {
    if (plugin.lifecycle === "listed") {
      return `<a href="${escapeHtml(safeExternalUrl(plugin.marketplaceUrl))}" target="_blank" rel="noreferrer">Marketplace</a>`;
    }
    return `<a href="${escapeHtml(safeExternalUrl(plugin.submissionUrl))}" target="_blank" rel="noreferrer">Review record</a>`;
  }

  function metricsRow(plugin) {
    if (!plugin.metrics) {
      return '<div class="metrics"><span>Marketplace decision pending</span></div>';
    }
    return `<div class="metrics" aria-label="Marketplace engagement">
      <span><strong>${compactNumber(plugin.metrics.views)}</strong> views</span>
      <span><strong>${compactNumber(plugin.metrics.copies)}</strong> copies</span>
      <span><strong>${compactNumber(plugin.metrics.hearts)}</strong> hearts</span>
    </div>`;
  }

  function pluginCard(plugin) {
    const review = plugin.lifecycle === "under-review";
    const statusLabel = review ? "In review" : "Listed";
    const copyButton = plugin.installCommand
      ? `<button type="button" data-copy-install="${escapeHtml(plugin.id)}">Copy install</button>`
      : "";
    return `<article class="plugin-card${review ? " review-card" : ""}" data-plugin-id="${escapeHtml(plugin.id)}">
      <div class="card-preview">
        <img src="${escapeHtml(safeExternalUrl(plugin.previewUrl))}" alt="${escapeHtml(plugin.name)} plugin interface preview" width="1280" height="720" loading="lazy">
      </div>
      <div class="card-body">
        <div class="card-meta">
          <span class="status-badge${review ? " review" : ""}">${statusLabel}</span>
          <span class="category-label">${escapeHtml(plugin.category)}</span>
        </div>
        <h3>${escapeHtml(plugin.name)}</h3>
        <p class="pitch">${escapeHtml(plugin.pitch)}</p>
        ${metricsRow(plugin)}
        <div class="card-actions">
          <a href="plugins/${encodeURIComponent(plugin.slug)}/">Details</a>
          ${marketplaceAction(plugin)}
          <a href="${escapeHtml(safeExternalUrl(plugin.repoUrl))}" target="_blank" rel="noreferrer">Source</a>
          ${copyButton}
        </div>
      </div>
    </article>`;
  }

  function filteredPlugins() {
    const query = state.query.trim().toLowerCase();
    return state.plugins.filter((plugin) => {
      const matchesStatus = state.status === "all" || plugin.lifecycle === state.status;
      const matchesCategory = state.category === "all" || plugin.category === state.category;
      const haystack = [plugin.name, plugin.pitch, plugin.category, ...(plugin.tags || [])].join(" ").toLowerCase();
      return matchesStatus && matchesCategory && (!query || haystack.includes(query));
    });
  }

  function wireCards() {
    grid.querySelectorAll("img").forEach((image) => {
      image.addEventListener("error", () => {
        image.hidden = true;
        image.parentElement.classList.add("image-missing");
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

  function setPressed(container, selector, selected) {
    container.querySelectorAll(selector).forEach((button) => {
      const active = button.dataset.status === selected || button.dataset.category === selected;
      button.classList.toggle("active", active);
      button.setAttribute("aria-pressed", String(active));
    });
  }

  function buildCategoryFilters(plugins) {
    const categories = [...new Set(plugins.map((plugin) => plugin.category))].sort();
    categoryFilters.innerHTML = ["all", ...categories].map((category) => {
      const label = category === "all" ? "Every category" : category;
      return `<button class="category-filter${category === "all" ? " active" : ""}" type="button" data-category="${escapeHtml(category)}" aria-pressed="${category === "all"}">${escapeHtml(label)}</button>`;
    }).join("");

    categoryFilters.addEventListener("click", (event) => {
      const button = event.target.closest("[data-category]");
      if (!button) return;
      state.category = button.dataset.category;
      setPressed(categoryFilters, "[data-category]", state.category);
      render();
    });
  }

  function formatFreshness(value) {
    const date = new Date(value);
    if (Number.isNaN(date.getTime())) return "current catalog snapshot";
    return new Intl.DateTimeFormat("en-US", {
      year: "numeric",
      month: "short",
      day: "numeric",
      timeZone: "UTC",
    }).format(date) + " UTC";
  }

  async function loadCatalog() {
    try {
      const response = await fetch("data/plugins.json", { cache: "no-store" });
      if (!response.ok) throw new Error(`Catalog request failed: ${response.status}`);
      const data = await response.json();
      if (!Array.isArray(data.plugins)) throw new Error("Catalog does not contain plugins");

      state.plugins = data.plugins;
      state.loadState = "ready";
      const listed = data.plugins.filter((plugin) => plugin.lifecycle === "listed").length;
      const inReview = data.plugins.filter((plugin) => plugin.lifecycle === "under-review").length;
      document.querySelector("#listed-count").textContent = listed;
      document.querySelector("#review-count").textContent = inReview;
      const reviewSummary = inReview === 0
        ? "no releases waiting on review"
        : `${inReview} ${inReview === 1 ? "release" : "releases"} in review`;
      document.querySelector("#catalog-summary").textContent = `${listed} official listings, ${reviewSummary}, and public source for every plugin.`;
      document.querySelector("#data-freshness").textContent = formatFreshness(data.generatedAt);
      const marketplaceAuthorUrl = safeExternalUrl(data.publisher.marketplaceUrl);
      const templateUrl = safeExternalUrl(data.template.repoUrl);
      if (marketplaceAuthorUrl) document.querySelector("#marketplace-author-link").href = marketplaceAuthorUrl;
      if (templateUrl) document.querySelector("#template-link").href = templateUrl;
      document.querySelector("#template-pitch").textContent = data.template.pitch;

      buildCategoryFilters(data.plugins);
      grid.setAttribute("aria-busy", "false");
      render();
    } catch (error) {
      state.loadState = "failed";
      grid.setAttribute("aria-busy", "false");
      const empty = document.createElement("div");
      empty.className = "empty-state";
      const heading = document.createElement("h3");
      heading.textContent = "The catalog could not load.";
      const detail = document.createElement("p");
      detail.textContent = error instanceof Error ? error.message : "Unknown catalog error";
      const repositoryLink = document.createElement("a");
      repositoryLink.href = "https://github.com/intent-solutions-io/omarchy-plugins";
      repositoryLink.textContent = "Open the repository catalog";
      empty.append(heading, detail, repositoryLink);
      grid.replaceChildren(empty);
      resultStatus.textContent = "Catalog unavailable";
    }
  }

  statusFilters.addEventListener("click", (event) => {
    const button = event.target.closest("[data-status]");
    if (!button) return;
    state.status = button.dataset.status;
    setPressed(statusFilters, "[data-status]", state.status);
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
