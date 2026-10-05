"""Focused AI-computer journeys. Run against a local static preview; APIs are mocked."""

import json
import os
from pathlib import Path

from playwright.sync_api import sync_playwright


def check_ai_interest(browser, base_url, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    for device, width, height in (("desktop", 1440, 1000), ("mobile", 390, 844)):
        page = browser.new_page(viewport={"width": width, "height": height})
        submissions, confirmations, errors = [], [], []
        page.on("pageerror", lambda error: errors.append(str(error)))

        def capture_interest(route):
            submissions.append(json.loads(route.request.post_data))
            route.fulfill(status=200, content_type="application/json", body=json.dumps({"status": "confirmation-required"}))

        def capture_confirmation(route):
            confirmations.append(json.loads(route.request.post_data))
            route.fulfill(status=200, content_type="application/json", body=json.dumps({"status": "confirmed"}))

        page.route("https://intentsolutions.io/api/forms/bluegold-interest", capture_interest)
        page.route("https://intentsolutions.io/api/forms/bluegold-confirm", capture_confirmation)
        page.goto(f"{base_url}/bluegoldblue/")
        page.wait_for_load_state("networkidle")
        page.locator(".bluegold-hero a[href='#local-ai-computer']").click()
        assert page.locator("#local-ai-title").is_visible()
        assert page.locator("#local-ai-computer details").count() == 3
        summary = page.locator("#local-ai-computer summary").first
        summary.focus()
        summary.press("Enter")
        assert page.locator("#local-ai-computer details").first.get_attribute("open") is not None
        summary.press("Enter")
        assert not page.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth")
        page.locator("#local-ai-computer").screenshot(
            path=output_dir / f"bluegold-ai-{device}.png",
            style=".skip-link { visibility: hidden; }",
        )
        if device == "desktop":
            page.evaluate("document.documentElement.style.zoom = '2'")
            assert not page.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth")
            page.evaluate("document.documentElement.style.zoom = '1'")
        cta = page.locator('[data-bluegold-offer="preconfigured-computer"]')
        cta.focus()
        cta.press("Enter")
        page.wait_for_function("document.activeElement.name === 'offer'")
        assert page.locator('[name="offer"]').input_value() == "preconfigured-computer"
        assert not page.locator('[name="consent"]').is_checked()
        assert submissions == []
        page.get_by_label("Name Required", exact=True).fill("Jordan Rivera")
        page.get_by_label("Email Required", exact=True).fill("jordan@example.test")
        page.get_by_role("button", name="Send my confirmation").click()
        assert submissions == []  # Consent is required even with a selected offer.
        page.locator('[name="consent"]').check()
        page.get_by_role("button", name="Send my confirmation").click()
        page.locator("#bluegold-receipt").wait_for(state="visible")
        assert submissions == [{
            "name": "Jordan Rivera", "email": "jordan@example.test",
            "offer": "preconfigured-computer", "journey": "not-sure",
            "currentOs": "not-sure", "blueStorage": "not-sure", "capacity": "not-sure",
            "timing": "researching", "consent": True,
            "consentVersion": "bluegold-interest-v1", "source": "website", "website": "",
        }]
        cta.click()
        assert page.locator("#bluegold-receipt").is_visible()
        assert page.locator("#bluegold-interest-form").is_hidden()
        assert len(submissions) == 1
        code = "AbCdEfGhIjKlMnOpQrStUv"
        page.goto(f"{base_url}/bluegoldblue/#c={code}")
        page.locator("#bluegold-confirmation").wait_for(state="visible")
        cta.click()
        assert page.locator("#bluegold-confirmation").is_visible()
        assert page.locator("#bluegold-interest-form").is_hidden()
        assert confirmations == []
        page.get_by_role("button", name="Confirm BLUE GOLD BLUE updates").click()
        page.get_by_text("Your interest is confirmed.", exact=False).wait_for()
        assert confirmations == [{"code": code}]
        assert code not in page.url
        cta.click()
        page.wait_for_function("document.activeElement.id === 'bluegold-confirmation-status'")
        assert len(confirmations) == 1
        assert not errors, errors
        page.close()

    for response in ({"status": "unexpected"}, {"error": "Try later"}):
        page = browser.new_page()
        page.route("https://intentsolutions.io/api/forms/bluegold-interest", lambda route: route.fulfill(
            status=200 if "status" in response else 503,
            content_type="application/json", body=json.dumps(response),
        ))
        page.goto(f"{base_url}/bluegoldblue/#local-ai-computer")
        page.locator('[data-bluegold-offer="preconfigured-computer"]').click()
        page.get_by_label("Name Required", exact=True).fill("Jordan Rivera")
        page.get_by_label("Email Required", exact=True).fill("jordan@example.test")
        page.locator('[name="consent"]').check()
        page.get_by_role("button", name="Send my confirmation").click()
        page.get_by_text("We could not confirm this submission", exact=False).wait_for()
        assert page.locator('[name="offer"]').input_value() == "preconfigured-computer"
        assert page.locator("#bluegold-receipt").is_hidden()
        page.close()

    page = browser.new_page(java_script_enabled=False)
    page.goto(f"{base_url}/bluegoldblue/#local-ai-computer")
    assert page.locator("#local-ai-title").is_visible()
    page.locator('[data-bluegold-offer="preconfigured-computer"]').click()
    page.locator('[name="offer"]').select_option("preconfigured-computer")
    assert page.locator('[name="offer"]').input_value() == "preconfigured-computer"
    page.close()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        try:
            check_ai_interest(browser, os.environ.get("OMA_SITE_BASE_URL", "http://127.0.0.1:4173"), Path("/tmp/oma-site-browser"))
        finally:
            browser.close()
    print("PASS: AI computer desktop/mobile, keyboard, consent, payload, confirmation, failures and no-JS content")
