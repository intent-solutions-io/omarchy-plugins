(() => {
  "use strict";

  document.querySelectorAll(".detail-preview img").forEach((image) => {
    const showUnavailable = () => {
      const preview = image.closest(".detail-preview");
      const source = image.parentElement;
      if (!source) return;
      const title = document.createElement("strong");
      title.textContent = "Preview unavailable";
      const action = document.createElement("span");
      action.textContent = "Open image source on GitHub";
      source.replaceChildren(title, action);
      preview.classList.add("preview-missing");
      preview.querySelector("figcaption").textContent = "The repository preview could not load.";
    };
    image.addEventListener("error", showUnavailable, { once: true });
    // A cached failure can finish before this deferred script runs.
    if (image.complete && image.naturalWidth === 0) showUnavailable();
  });

  const button = document.querySelector("[data-detail-copy]");
  const toast = document.querySelector("#toast");
  if (!button) return;

  button.addEventListener("click", async () => {
    const command = document.body.dataset.installCommand;
    if (!command) return;
    try {
      await navigator.clipboard.writeText(command);
      toast.textContent = "Install command copied";
    } catch {
      toast.textContent = "Copy failed. Select the command manually.";
    }
    toast.classList.add("visible");
    window.setTimeout(() => toast.classList.remove("visible"), 2200);
  });
})();
