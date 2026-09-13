(() => {
  "use strict";

  const form = document.querySelector("#bluegold-interest-form");
  const status = document.querySelector("#bluegold-form-status");
  const confirmation = document.querySelector("#bluegold-confirmation");
  const confirmationButton = document.querySelector("#bluegold-confirm-button");
  const confirmationStatus = document.querySelector("#bluegold-confirmation-status");
  if (!form || !status || !confirmation || !confirmationButton || !confirmationStatus) return;

  const endpoint = "https://intentsolutions.io/api/forms/bluegold-interest";
  const confirmationEndpoint = "https://intentsolutions.io/api/forms/bluegold-confirm";
  const consentVersion = "bluegold-interest-v1";
  const submit = form.querySelector('button[type="submit"]');
  const defaultLabel = submit.textContent;

  function source() {
    const value = new URLSearchParams(window.location.search).get("utm_source")?.toLowerCase() || "website";
    return /^[a-z0-9][a-z0-9_-]{0,39}$/.test(value) ? value : "website";
  }

  function setState(target, message, state) {
    target.textContent = message;
    target.dataset.state = state;
  }

  function revealOutcome(focusTarget) {
    window.requestAnimationFrame(() => {
      document.querySelector("#interest")?.scrollIntoView({ block: "start" });
      focusTarget.focus({ preventScroll: true });
    });
  }

  let confirmationCode = null;
  let legacyConfirmationToken = null;
  let confirmationCredential = null;

  function readConfirmationRoute() {
    const outcome = new URLSearchParams(window.location.search).get("interest");
    const confirmationParams = new URLSearchParams(window.location.hash.slice(1));
    confirmationCode = confirmationParams.get("c");
    legacyConfirmationToken = confirmationParams.get("token");
    confirmationCredential = confirmationCode || legacyConfirmationToken;
    if (confirmationCode || outcome === "confirm") {
      if (!confirmationCredential) {
        setState(status, "That confirmation link is incomplete. Submit the form again for a new link.", "error");
        revealOutcome(status);
      } else {
        form.hidden = true;
        confirmation.hidden = false;
        revealOutcome(confirmationButton);
      }
    } else if (outcome === "confirmed") {
      setState(status, "Your interest is confirmed. We will only contact you about BLUE GOLD BLUE.", "success");
      revealOutcome(status);
    } else if (outcome === "invalid") {
      setState(status, "That confirmation link is invalid or expired. Submit the form again for a new link.", "error");
      revealOutcome(status);
    }
  }

  readConfirmationRoute();
  window.addEventListener("hashchange", readConfirmationRoute);

  confirmationButton.addEventListener("click", async () => {
    if (!confirmationCredential) return;
    confirmationButton.disabled = true;
    confirmationButton.textContent = "Confirming...";
    setState(confirmationStatus, "Confirming your BLUE GOLD BLUE interest.", "loading");
    try {
      const response = await fetch(confirmationEndpoint, {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(confirmationCode
          ? { code: confirmationCode }
          : { token: legacyConfirmationToken }),
      });
      const result = await response.json().catch(() => ({}));
      if (!response.ok) throw new Error(result.error || "The confirmation service did not respond.");
      confirmationButton.hidden = true;
      setState(confirmationStatus, "Your interest is confirmed. We will only contact you about BLUE GOLD BLUE.", "success");
      window.history.replaceState({}, "", "?interest=confirmed#interest");
      revealOutcome(confirmationStatus);
    } catch (error) {
      setState(confirmationStatus, `${error.message} Try again, or request a new confirmation link below.`, "error");
      confirmationButton.disabled = false;
      confirmationButton.textContent = "Try confirmation again";
      revealOutcome(confirmationStatus);
    }
  });

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;

    const data = new FormData(form);
    const payload = {
      name: String(data.get("name") || "").trim(),
      email: String(data.get("email") || "").trim(),
      offer: String(data.get("offer") || ""),
      journey: String(data.get("journey") || "not-sure"),
      currentOs: String(data.get("currentOs") || "not-sure"),
      blueStorage: String(data.get("blueStorage") || "not-sure"),
      capacity: String(data.get("capacity") || "not-sure"),
      timing: String(data.get("timing") || "researching"),
      consent: data.get("consent") === "on",
      consentVersion,
      source: source(),
      website: String(data.get("website") || ""),
    };

    submit.disabled = true;
    submit.textContent = "Sending confirmation...";
    setState(status, "Sending a confirmation link to the email provided.", "loading");

    try {
      const response = await fetch(endpoint, {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(payload),
      });
      const result = await response.json().catch(() => ({}));
      if (!response.ok) throw new Error(result.error || "The interest service did not respond.");
      form.reset();
      setState(status, "Check your email and confirm within 48 hours. Nothing is added to the interest list until you confirm.", "success");
    } catch (error) {
      setState(status, `${error.message} Your information was not added. Please try again.`, "error");
    } finally {
      submit.disabled = false;
      submit.textContent = defaultLabel;
    }
  });
})();
