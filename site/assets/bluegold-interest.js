(() => {
  "use strict";

  const form = document.querySelector("#bluegold-interest-form");
  const status = document.querySelector("#bluegold-form-status");
  const confirmation = document.querySelector("#bluegold-confirmation");
  const confirmationButton = document.querySelector("#bluegold-confirm-button");
  const confirmationStatus = document.querySelector("#bluegold-confirmation-status");
  const receipt = document.querySelector("#bluegold-receipt");
  const receiptTitle = document.querySelector("#bluegold-receipt-title");
  const receiptEmail = document.querySelector("#bluegold-receipt-email");
  const restartButton = document.querySelector("#bluegold-restart-button");
  if (!form || !status || !confirmation || !confirmationButton || !confirmationStatus
    || !receipt || !receiptTitle || !receiptEmail || !restartButton) return;

  const endpoint = "https://intentsolutions.io/api/forms/bluegold-interest";
  const confirmationEndpoint = "https://intentsolutions.io/api/forms/bluegold-confirm";
  const consentVersion = "bluegold-interest-v1";
  const confirmationCodePattern = /^[A-Za-z0-9_-]{22}$/;
  const submit = form.querySelector('button[type="submit"]');
  const defaultLabel = submit.textContent;
  const defaultConfirmationLabel = confirmationButton.textContent;
  let interestAccepted = false;

  async function postJson(url, payload, expectedStatus) {
    const controller = new AbortController();
    const timeout = window.setTimeout(() => controller.abort(), 30000);
    try {
      const response = await fetch(url, {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(payload),
        signal: controller.signal,
      });
      const result = await response.json().catch((error) => {
        if (error.name === "AbortError") throw error;
        return {};
      });
      if (!response.ok) throw new Error(result?.error || "The service could not accept your request.");
      if (result?.status !== expectedStatus) throw new Error("We could not verify the service response.");
      return result;
    } catch (error) {
      if (error.name === "AbortError") throw new Error("The request took too long to respond.");
      throw error;
    } finally {
      window.clearTimeout(timeout);
    }
  }

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
      focusTarget.scrollIntoView({ block: "center", behavior: "instant" });
      focusTarget.focus({ preventScroll: true });
    });
  }

  let confirmationCode = null;
  let legacyConfirmationToken = null;
  let confirmationCredential = null;

  function resetConfirmationView() {
    form.hidden = interestAccepted;
    receipt.hidden = !interestAccepted;
    confirmation.hidden = true;
    confirmationButton.hidden = false;
    confirmationButton.disabled = false;
    confirmationButton.textContent = defaultConfirmationLabel;
    setState(confirmationStatus, "", "idle");
  }

  function readConfirmationRoute() {
    const outcome = new URLSearchParams(window.location.search).get("interest");
    const confirmationParams = new URLSearchParams(window.location.hash.slice(1));
    const hasConfirmationCode = confirmationParams.has("c");
    confirmationCode = hasConfirmationCode ? confirmationParams.get("c") : null;
    legacyConfirmationToken = confirmationParams.get("token");
    confirmationCredential = confirmationCodePattern.test(confirmationCode || "")
      ? confirmationCode
      : legacyConfirmationToken;
    resetConfirmationView();
    if (hasConfirmationCode || outcome === "confirm") {
      if (!confirmationCredential) {
        setState(status, "That confirmation link is incomplete. Submit the form again for a new link.", "error");
        revealOutcome(status);
      } else {
        form.hidden = true;
        receipt.hidden = true;
        confirmation.hidden = false;
        revealOutcome(confirmationButton);
      }
    } else if (outcome === "confirmed") {
      setState(status, "Your interest is confirmed. We will only contact you about BLUE GOLD BLUE.", "success");
      revealOutcome(status);
    } else if (outcome === "invalid") {
      setState(status, "That confirmation link is invalid or expired. Submit the form again for a new link.", "error");
      revealOutcome(status);
    } else {
      confirmationCode = null;
      legacyConfirmationToken = null;
      confirmationCredential = null;
    }
  }

  readConfirmationRoute();
  window.addEventListener("hashchange", readConfirmationRoute);

  restartButton.addEventListener("click", () => {
    interestAccepted = false;
    resetConfirmationView();
    setState(status, "", "idle");
    revealOutcome(form.querySelector('[name="email"]'));
  });

  confirmationButton.addEventListener("click", async () => {
    if (!confirmationCredential) return;
    confirmationButton.disabled = true;
    confirmationButton.textContent = "Confirming...";
    setState(confirmationStatus, "Confirming your BLUE GOLD BLUE interest.", "loading");
    try {
      await postJson(confirmationEndpoint, confirmationCode
        ? { code: confirmationCode }
        : { token: legacyConfirmationToken }, "confirmed");
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
      await postJson(endpoint, payload, "confirmation-required");
      form.reset();
      interestAccepted = true;
      receiptEmail.textContent = `We sent a confirmation link to ${payload.email}.`;
      form.hidden = true;
      receipt.hidden = false;
      revealOutcome(receiptTitle);
    } catch (error) {
      setState(status, `${error.message} We could not confirm this submission. Your entries are still here. Check your inbox before trying again, or contact support@intentsolutions.io.`, "error");
      revealOutcome(status);
    } finally {
      submit.disabled = false;
      submit.textContent = defaultLabel;
    }
  });
})();
