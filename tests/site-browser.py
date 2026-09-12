import copy
import json
import os
from pathlib import Path

from playwright.sync_api import sync_playwright


BASE_URL = os.environ.get("OMA_SITE_BASE_URL", "http://127.0.0.1:4173")
OUTPUT_DIR = Path("/tmp/oma-site-browser")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
DATA = json.loads((Path(__file__).parents[1] / "site/data/plugins.json").read_text())
PLUGINS = DATA["plugins"]


def assert_no_overflow(page) -> None:
    assert not page.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth")


def assert_catalog(page, *, mobile: bool = False) -> None:
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    page.locator(".plugin-card").first.wait_for()

    assert "Intent Solutions" in page.locator(".wordmark").inner_text()
    assert "Omarchy Plugins" in page.locator(".wordmark").inner_text()
    assert page.locator(".wordmark-mark").count() == 0
    assert page.locator(".plugin-card").count() == len(PLUGINS)
    assert f"{len(PLUGINS)} official listings" in page.locator("#catalog-summary").inner_text()
    assert page.locator("#plugin-grid").get_attribute("aria-busy") == "false"
    assert page.locator(".source-facts").count() == len(PLUGINS)
    assert page.locator(".manifest-aligned").count() == len(PLUGINS)
    assert page.locator("#featured-project").count() == 1
    assert page.get_by_role("link", name="Play The Beacon Wakes").get_attribute("href") == "the-beacon-wakes/play/"
    assert page.locator('[data-plugin-id="io.github.jeremylongshore.omatrail"] a', has_text="Details").get_attribute("href") == "plugins/omatrail/"
    assert page.get_by_role("link", name="Help maintain a plugin").count() == 1
    assert_no_overflow(page)

    if mobile:
        page.screenshot(path=OUTPUT_DIR / "mobile.png", full_page=True)
        return

    page.keyboard.press("/")
    assert page.evaluate("document.activeElement.id") == "plugin-search"
    page.locator("#plugin-search").fill("MLB")
    assert page.locator(".plugin-card").count() == 1
    assert page.locator(".plugin-card h3").inner_text() == "MLB Booth"
    page.keyboard.press("Escape")
    assert page.locator(".plugin-card").count() == len(PLUGINS)

    page.get_by_role("button", name="Sports", exact=True).click()
    assert page.locator(".plugin-card").count() == 2
    page.get_by_role("button", name="Every family", exact=True).click()

    page.locator("#plugin-search").fill("zzzz-no-result")
    assert page.locator(".plugin-card").count() == 0
    assert page.get_by_text("No plugins match those filters.").count() == 1
    page.locator("#plugin-search").fill("")

    copy_button = page.locator('[data-copy-install="io.github.jeremylongshore.bazaar"]')
    copy_button.click()
    copied = page.evaluate("navigator.clipboard.readText()")
    assert copied == "omarchy plugin add https://github.com/jeremylongshore/omarchy-bazaar-entry.git --enable"
    page.screenshot(path=OUTPUT_DIR / "desktop.png", full_page=True)


def assert_nonlisted_edge_case(context) -> None:
    fake_data = copy.deepcopy(DATA)
    plugin = fake_data["plugins"][0]
    plugin.update({
        "lifecycle": "developing",
        "marketplaceUrl": None,
        "submissionUrl": None,
        "installCommand": None,
        "metrics": None,
        "pitch": "Build signals across sport, art, العربية, 日本語, and robotics 🚀 " + "without turning the catalogue into homework. " * 7,
        "previewUrl": None,
        "preview": {"status": "missing", "url": None, "path": "preview.png", "sha": None},
        "manifest": {"status": "drift", "version": "0.1.0", "sha": "c" * 40, "issues": ["version differs"]},
    })
    fake_data["plugins"] = [plugin]
    page = context.new_page()
    page.route("**/data/plugins.json", lambda route: route.fulfill(status=200, content_type="application/json", body=json.dumps(fake_data)))
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    page.locator(".plugin-card").wait_for()
    assert page.get_by_text("Developing", exact=True).count() >= 1
    assert page.get_by_text("Preview unavailable", exact=True).count() == 1
    assert page.locator(".manifest-drift").count() == 1
    assert page.locator(".plugin-card").get_by_role("link", name="Marketplace").count() == 0
    assert page.locator(".plugin-card").get_by_role("link", name="Review record").count() == 0
    assert page.locator(".plugin-card").get_by_role("button", name="Copy install").count() == 0
    assert "العربية" in page.locator(".pitch").inner_text()
    assert_no_overflow(page)
    page.close()


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    desktop_context = browser.new_context(
        viewport={"width": 1440, "height": 1000},
        device_scale_factor=1,
        permissions=["clipboard-read", "clipboard-write"],
    )
    desktop_errors = []
    desktop = desktop_context.new_page()
    desktop.on("console", lambda message: desktop_errors.append(message.text) if message.type == "error" else None)
    assert_catalog(desktop)
    assert not desktop_errors, desktop_errors

    mobile_errors = []
    mobile = browser.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=1)
    mobile.on("console", lambda message: mobile_errors.append(message.text) if message.type == "error" else None)
    assert_catalog(mobile, mobile=True)
    assert not mobile_errors, mobile_errors

    for width, height in ((375, 812), (768, 1024), (1024, 768)):
        responsive = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=1)
        responsive.goto(BASE_URL)
        responsive.wait_for_load_state("networkidle")
        responsive.locator(".plugin-card").first.wait_for()
        assert responsive.locator(".plugin-card").count() == len(PLUGINS)
        assert_no_overflow(responsive)
        responsive.close()

    assert_nonlisted_edge_case(desktop_context)

    social = browser.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=1)
    social.goto(BASE_URL)
    social.wait_for_load_state("networkidle")
    social.evaluate("window.scrollTo(0, 0)")
    social.screenshot(path="site/assets/og-card.png")

    detail_errors = []
    detail = desktop_context.new_page()
    detail.on("console", lambda message: detail_errors.append(message.text) if message.type == "error" else None)
    for plugin in PLUGINS:
        detail.goto(f"{BASE_URL}/plugins/{plugin['slug']}/")
        detail.wait_for_load_state("networkidle")
        assert detail.locator("h1").inner_text() == plugin["name"]
        assert detail.get_by_text("Officially listed", exact=True).count() == 1
        assert detail.locator('[data-manifest-status="aligned"]').count() == 1
        assert detail.locator("[data-detail-copy]").count() == 1
        assert_no_overflow(detail)
        assert detail.locator(".detail-preview img").evaluate("image => image.complete && image.naturalWidth > 0")
        if plugin["slug"] in {"bazaar", "omatrail"}:
            detail.evaluate("window.scrollTo(0, 0)")
            detail.screenshot(path=OUTPUT_DIR / f"detail-{plugin['slug']}.png", full_page=True)
        detail.locator("[data-detail-copy]").click()
        assert detail.evaluate("navigator.clipboard.readText()") == plugin["installCommand"]
    assert not detail_errors, detail_errors

    for plugin in PLUGINS:
        mobile.goto(f"{BASE_URL}/plugins/{plugin['slug']}/")
        mobile.wait_for_load_state("networkidle")
        assert mobile.locator("h1").inner_text() == plugin["name"]
        assert_no_overflow(mobile)

    for page, viewport, filename in (
        (desktop_context.new_page(), {"width": 1440, "height": 1000}, "beacon-desktop.png"),
        (browser.new_page(viewport={"width": 390, "height": 844}), {"width": 390, "height": 844}, "beacon-mobile.png"),
    ):
        submitted_signup = {}
        if filename == "beacon-desktop.png":
            def capture_signup(route):
                submitted_signup.update(json.loads(route.request.post_data))
                route.fulfill(status=200, content_type="application/json", body=json.dumps({"status": "confirmation-required"}))

            page.route("https://intentsolutions.io/api/forms/beacon-signup", capture_signup)
            confirmed_token = {}
            def capture_confirmation(route):
                confirmed_token.update(json.loads(route.request.post_data))
                route.fulfill(status=200, content_type="application/json", body=json.dumps({"status": "confirmed"}))

            page.route("https://intentsolutions.io/api/forms/beacon-confirm", capture_confirmation)
        page.set_viewport_size(viewport)
        page.goto(f"{BASE_URL}/the-beacon-wakes/")
        page.wait_for_load_state("networkidle")
        assert page.get_by_role("heading", name="The Beacon Wakes").count() == 1
        assert page.locator("#parent-guide").count() == 1
        assert page.locator("#parent-updates").count() == 1
        assert page.get_by_text("No email required", exact=True).count() == 1
        if filename == "beacon-mobile.png":
            assert page.get_by_role("link", name="Release updates").is_visible()
        if filename == "beacon-desktop.png":
            page.locator('[name="firstName"]').fill("Jordan")
            page.locator('[name="lastName"]').fill("Rivera")
            page.locator('[name="email"]').fill("parent@example.test")
            page.locator('[name="consent"]').check()
            page.get_by_role("button", name="Send my confirmation").click()
            page.get_by_text("Check your email and confirm within 48 hours.", exact=False).wait_for()
            assert submitted_signup == {
                "firstName": "Jordan",
                "lastName": "Rivera",
                "email": "parent@example.test",
                "consent": True,
                "consentVersion": "beacon-release-updates-v1",
                "source": "website",
                "website": "",
            }
            page.evaluate("document.documentElement.style.scrollBehavior = 'auto'; window.scrollTo(0, 0)")
            page.locator(".skip-link").evaluate("element => element.style.display = 'none'")
            page.screenshot(path=OUTPUT_DIR / filename, full_page=True)
            page.goto(f"{BASE_URL}/the-beacon-wakes/?signup=confirm#token=sealed-test-token")
            page.get_by_role("button", name="Confirm release updates").wait_for()
            assert page.locator("#beacon-signup").is_hidden()
            assert page.locator("#beacon-confirm-button").evaluate("element => document.activeElement === element")
            page.locator(".skip-link").evaluate("element => element.style.display = 'none'")
            page.screenshot(path=OUTPUT_DIR / "beacon-confirm-desktop.png", full_page=True)
            page.get_by_role("button", name="Confirm release updates").click()
            page.get_by_text("You are confirmed.", exact=False).wait_for()
            assert confirmed_token == {"token": "sealed-test-token"}
            assert "sealed-test-token" not in page.url
            page.goto(f"{BASE_URL}/the-beacon-wakes/?signup=invalid")
            page.get_by_text("That confirmation link is invalid or expired.", exact=False).wait_for()
            assert page.locator("#beacon-form-status").evaluate("element => document.activeElement === element")
            page.wait_for_function("document.querySelector('#parent-updates').getBoundingClientRect().top < innerHeight / 3")
        assert_no_overflow(page)
        if filename != "beacon-desktop.png":
            page.screenshot(path=OUTPUT_DIR / filename, full_page=True)
        page.close()

    demo = browser.new_page(viewport={"width": 1440, "height": 900})
    demo.goto(f"{BASE_URL}/the-beacon-wakes/play/")
    demo.wait_for_load_state("networkidle")
    assert demo.get_by_role("heading", name="The Beacon Wakes").count() == 1
    demo.get_by_role("button", name="Press Enter to launch demo").click()
    demo.keyboard.type("find the quiet frequency")
    demo.keyboard.type("wake the field receiver")
    assert demo.locator("#completion-stamp").inner_text() == "SIGNAL TRAIL ONLINE"
    assert demo.locator("#result-signals").inner_text() == "2"
    assert demo.get_by_role("button", name="Parent: see the full game").count() == 1
    assert_no_overflow(demo)
    demo.screenshot(path=OUTPUT_DIR / "beacon-demo-complete.png", full_page=True)
    demo.close()

    mobile_demo = browser.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=1)
    mobile_demo.goto(f"{BASE_URL}/the-beacon-wakes/play/")
    mobile_demo.wait_for_load_state("networkidle")
    mobile_demo.get_by_role("button", name="Press Enter to launch demo").click()
    touch_input = mobile_demo.get_by_role("textbox", name="Phone or tablet keyboard")
    assert touch_input.is_visible()
    assert_no_overflow(mobile_demo)
    mobile_demo.screenshot(path=OUTPUT_DIR / "beacon-demo-mobile.png", full_page=True)
    mobile_demo.close()

    legacy = browser.new_page()
    legacy.goto(f"{BASE_URL}/omaquest/")
    legacy.wait_for_url(f"{BASE_URL}/the-beacon-wakes/")
    assert legacy.get_by_role("heading", name="The Beacon Wakes").count() == 1
    legacy.close()

    legal_expectations = {
        "privacy": ("privacy", "Privacy Policy"),
        "app-privacy": ("app-privacy", "Privacy Policy"),
        "acceptable-use": ("acceptable-use", "Acceptable Use Policy"),
        "terms": ("terms-of-service", "Terms and Conditions"),
    }
    for route, (document, heading) in legal_expectations.items():
        legal = browser.new_page(viewport={"width": 1440, "height": 1000})
        legal.goto(f"{BASE_URL}/{route}/")
        legal.locator(".getterms-document-embed h1").wait_for(timeout=60000)
        assert legal.locator(".getterms-document-embed").get_attribute("data-getterms-document") == document
        assert heading.casefold() in legal.locator(".getterms-document-embed h1").inner_text().casefold()
        rendered = legal.locator(".getterms-document-embed").inner_text()
        assert "No You Pick" not in rendered
        assert "diagnosticpro.reports@gmail.com" not in rendered
        assert "We do not aim any of our products or services directly at children under the age of 13" not in rendered
        assert legal.get_by_role("navigation", name="Legal", exact=True).count() == 1
        assert_no_overflow(legal)
        if route == "privacy":
            legal.evaluate("window.scrollTo(0, 0)")
            legal.screenshot(path=OUTPUT_DIR / "legal-privacy-desktop.png", full_page=True)
        legal.close()

    legal_mobile = browser.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=1)
    legal_mobile.goto(f"{BASE_URL}/acceptable-use/")
    legal_mobile.locator(".getterms-document-embed h1").wait_for(timeout=60000)
    assert_no_overflow(legal_mobile)
    legal_mobile.screenshot(path=OUTPUT_DIR / "legal-acceptable-use-mobile.png", full_page=True)
    legal_mobile.close()

    failed = desktop_context.new_page()
    failed.route("**/data/plugins.json", lambda route: route.fulfill(status=200, content_type="application/json", body=json.dumps({"plugins": [{"name": "bad"}]})))
    failed.goto(BASE_URL)
    failed.wait_for_load_state("networkidle")
    assert failed.get_by_text("The catalogue could not load.").count() == 1
    failed.locator("#plugin-search").fill("test")
    assert failed.get_by_text("The catalogue could not load.").count() == 1

    browser.close()

print(f"PASS: browser checks and screenshots written to {OUTPUT_DIR}")
