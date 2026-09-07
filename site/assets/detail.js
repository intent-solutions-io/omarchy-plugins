(() => {
  "use strict";

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
