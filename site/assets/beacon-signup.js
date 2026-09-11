(() => {
  "use strict";

  const form = document.querySelector("#beacon-signup");
  const status = document.querySelector("#beacon-form-status");
  if (!form || !status) return;

  const endpoint = "https://intentsolutions.io/api/forms/beacon-signup";
  const consentVersion = "beacon-release-updates-v1";
  const submit = form.querySelector('button[type="submit"]');
  const defaultLabel = submit.textContent;

  function source() {
    const value = new URLSearchParams(window.location.search).get("utm_source")?.toLowerCase() || "website";
    return /^[a-z0-9][a-z0-9_-]{0,39}$/.test(value) ? value : "website";
  }

  function setState(message, state) {
    status.textContent = message;
    status.dataset.state = state;
  }

  function revealOutcome() {
    const section = document.querySelector("#parent-updates");
    window.requestAnimationFrame(() => {
      section?.scrollIntoView({ block: "start" });
      status.focus({ preventScroll: true });
    });
  }

  const outcome = new URLSearchParams(window.location.search).get("signup");
  if (outcome === "confirmed") {
    setState("You are confirmed. The next release update will come by email.", "success");
    revealOutcome();
  } else if (outcome === "invalid") {
    setState("That confirmation link is invalid or expired. Submit the form again for a new link.", "error");
    revealOutcome();
  }

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;

    const data = new FormData(form);
    const payload = {
      firstName: String(data.get("firstName") || "").trim(),
      lastName: String(data.get("lastName") || "").trim(),
      email: String(data.get("email") || "").trim(),
      consent: data.get("consent") === "on",
      consentVersion,
      source: source(),
      website: String(data.get("website") || ""),
    };

    submit.disabled = true;
    submit.textContent = "Sending confirmation...";
    setState("Sending a confirmation link to the parent email provided.", "loading");

    try {
      const response = await fetch(endpoint, {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(payload),
      });
      const result = await response.json().catch(() => ({}));
      if (!response.ok) throw new Error(result.error || "The signup service did not respond.");
      form.reset();
      setState("Check your email and confirm within 48 hours. Nothing is added to the release list until you confirm.", "success");
    } catch (error) {
      setState(`${error.message} Your information was not added. Please try again.`, "error");
    } finally {
      submit.disabled = false;
      submit.textContent = defaultLabel;
    }
  });
})();
