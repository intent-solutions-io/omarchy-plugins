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
LIVE_STATS = {
    "plugins": {
        plugin["id"]: {
            "views": (plugin.get("metrics") or {}).get("views", 0) + 7,
            "copies": (plugin.get("metrics") or {}).get("copies", 0) + 1,
            "hearts": (plugin.get("metrics") or {}).get("hearts", 0),
        }
        for plugin in PLUGINS
    }
}


def mock_live_metrics(page) -> None:
    page.route(
        "https://api.omarchyplugins.com/v1/stats",
        lambda route: route.fulfill(status=200, content_type="application/json", body=json.dumps(LIVE_STATS)),
    )


def mock_perception_api(page) -> None:
    page.route(
        "https://api.perception.intentsolutions.io/**",
        lambda route: route.fulfill(status=202, content_type="application/json", body="{}"),
    )


def assert_no_overflow(page) -> None:
    assert not page.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth")


def assert_catalog(page, *, mobile: bool = False) -> None:
    mock_live_metrics(page)
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    page.locator(".plugin-card").first.wait_for()

    assert "Intent Solutions" in page.locator(".wordmark").inner_text()
    assert "Omarchy Plugins" in page.locator(".wordmark").inner_text()
    assert page.locator(".wordmark-mark").count() == 0
    assert page.locator(".plugin-card").count() == len(PLUGINS)
    assert f"{len(PLUGINS)} official listings" in page.locator("#catalog-summary").inner_text()
    assert "1 linked project" in page.locator("#catalog-summary").inner_text()
    assert page.locator("#project-count").inner_text() == "1"
    assert page.locator("#plugin-grid").get_attribute("aria-busy") == "false"
    assert page.locator(".source-facts").count() == len(PLUGINS)
    assert page.locator(".manifest-aligned").count() == len(PLUGINS)
    assert page.locator("#featured-project").count() == 1
    assert page.get_by_role("link", name="Play The Beacon Wakes").get_attribute("href") == "the-beacon-wakes/play/"
    assert page.locator('[data-plugin-id="io.github.jeremylongshore.omatrail"] a', has_text="Details").get_attribute("href") == "plugins/omatrail/"
    listening_post = page.locator('[data-plugin-id="io.github.jeremylongshore.listening-post"]')
    assert listening_post.get_by_role("link", name="Open Perception").get_attribute("href") == "/perception/"
    assert "live counters" in page.locator("#data-freshness").inner_text()
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
    mock_live_metrics(page)
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
        mock_live_metrics(responsive)
        responsive.goto(BASE_URL)
        responsive.wait_for_load_state("networkidle")
        responsive.locator(".plugin-card").first.wait_for()
        assert responsive.locator(".plugin-card").count() == len(PLUGINS)
        assert_no_overflow(responsive)
        responsive.close()

    assert_nonlisted_edge_case(desktop_context)

    social = browser.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=1)
    mock_live_metrics(social)
    social.goto(BASE_URL)
    social.wait_for_load_state("networkidle")
    social.evaluate("window.scrollTo(0, 0)")
    social.screenshot(path="site/assets/og-card.png")

    perception_errors = []
    for viewport, filename in (
        ({"width": 1440, "height": 1000}, "perception-desktop.png"),
        ({"width": 390, "height": 844}, "perception-mobile.png"),
    ):
        perception = browser.new_page(viewport=viewport, device_scale_factor=1)
        perception.on("console", lambda message: perception_errors.append(message.text) if message.type == "error" else None)
        mock_perception_api(perception)
        perception.goto(f"{BASE_URL}/perception/")
        perception.wait_for_load_state("networkidle")
        assert perception.get_by_role("heading", name="Stop checking feeds. Let the signal come to you.").count() == 1
        assert_no_overflow(perception)
        perception.screenshot(path=OUTPUT_DIR / filename, full_page=True)
        perception.close()
    assert not perception_errors, perception_errors

    perception_social = browser.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=1)
    perception_social.goto(f"{BASE_URL}/perception/")
    perception_social.wait_for_load_state("networkidle")
    perception_social.screenshot(path="site/assets/perception-card.png")
    perception_social.close()

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
            page.wait_for_url(f"{BASE_URL}/the-beacon-wakes/thanks/")
            assert page.get_by_role("heading", name="Check your email.").count() == 1
            assert page.get_by_text("Nothing is added to the release list", exact=False).count() == 1
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

    for page, viewport, filename in (
        (desktop_context.new_page(), {"width": 1440, "height": 1000}, "bluegold-desktop.png"),
        (browser.new_page(viewport={"width": 390, "height": 844}), {"width": 390, "height": 844}, "bluegold-mobile.png"),
    ):
        submitted_interest = {}
        confirmed_interest = {}
        if filename == "bluegold-desktop.png":
            def capture_interest(route):
                submitted_interest.update(json.loads(route.request.post_data))
                route.fulfill(status=200, content_type="application/json", body=json.dumps({"status": "confirmation-required"}))

            def capture_interest_confirmation(route):
                confirmed_interest.update(json.loads(route.request.post_data))
                route.fulfill(status=200, content_type="application/json", body=json.dumps({"status": "confirmed"}))

            page.route("https://intentsolutions.io/api/forms/bluegold-interest", capture_interest)
            page.route("https://intentsolutions.io/api/forms/bluegold-confirm", capture_interest_confirmation)
        page.set_viewport_size(viewport)
        page.goto(f"{BASE_URL}/bluegoldblue/")
        page.wait_for_load_state("networkidle")
        assert page.get_by_role("heading", name="Windows to Omarchy. Bring your stuff with you.").count() == 1
        assert page.get_by_text("GOLD is the key", exact=False).count() == 1
        assert page.get_by_text("a physical storage device you keep", exact=False).count() == 1
        assert page.get_by_text("256 GB", exact=True).count() == 1
        assert page.get_by_text("Keep BLUE as your backup", exact=True).count() == 1
        assert page.get_by_text("WELCOME local assistant", exact=True).count() == 1
        assert page.get_by_text("BLUE BEFORE GOLD. ALWAYS.", exact=True).count() == 1
        assert page.locator(".bluegold-honesty strong").inner_text() == "Still in research and development. Not for sale yet."
        faq_entries = page.locator("#faq details")
        assert faq_entries.count() == 66
        for index in range(faq_entries.count()):
            entry = faq_entries.nth(index)
            assert entry.locator("summary").count() == 1
            assert entry.locator(".bluegold-answer-state").count() == 1
            assert entry.locator(":scope > div").text_content().strip()
        assert page.locator(".bluegold-faq-map a").count() == 5
        faq_targets = page.locator(".bluegold-faq-map a").evaluate_all(
            "links => links.map(link => link.hash.slice(1))",
        )
        assert faq_targets == ["faq-start", "faq-computer", "faq-data", "faq-safety", "faq-after"]
        assert len(faq_targets) == len(set(faq_targets))
        for target in faq_targets:
            assert page.locator(f"#{target}").count() == 1
        first_question = page.locator("#faq details summary").first
        first_question.focus()
        assert first_question.evaluate("element => document.activeElement === element")
        first_question.press("Enter")
        assert faq_entries.first.get_attribute("open") is not None
        first_question.press("Enter")
        assert faq_entries.first.get_attribute("open") is None
        page.get_by_role("link", name="Your stuff Files, apps, and accounts").click()
        assert page.locator("#faq-data").evaluate("element => element.id") == "faq-data"
        destructive_question = page.get_by_text("Will GOLD remove Windows from my computer?", exact=True)
        destructive_question.click()
        destructive_answer = page.get_by_text("On the same-computer journey, yes.", exact=False)
        assert destructive_answer.is_visible()
        destructive_question.press("Enter")
        assert destructive_answer.is_hidden()
        assert page.get_by_role("link", name="Privacy", exact=True).count() >= 1
        assert_no_overflow(page)
        if filename == "bluegold-desktop.png":
            page.get_by_label("Name Required", exact=True).fill("Jordan Rivera")
            page.get_by_label("Email Required", exact=True).fill("jordan@example.test")
            page.get_by_label("Which concept interests you most?").select_option("blue-gold-kit")
            page.get_by_label("Which journey fits?").select_option("new-computer")
            page.get_by_label("Current Windows version").select_option("windows-11")
            page.get_by_label("Preferred BLUE storage").select_option("premium-blue-ssd")
            page.get_by_label("Estimated data to keep").select_option("512gb-1tb")
            page.get_by_label("When would this matter?").select_option("when-proven")
            page.locator('[name="consent"]').check()
            page.get_by_role("button", name="Send my confirmation").click()
            page.get_by_text("Check your email and confirm within 48 hours.", exact=False).wait_for()
            assert submitted_interest == {
                "name": "Jordan Rivera",
                "email": "jordan@example.test",
                "offer": "blue-gold-kit",
                "journey": "new-computer",
                "currentOs": "windows-11",
                "blueStorage": "premium-blue-ssd",
                "capacity": "512gb-1tb",
                "timing": "when-proven",
                "consent": True,
                "consentVersion": "bluegold-interest-v1",
                "source": "website",
                "website": "",
            }
            page.evaluate("document.documentElement.style.scrollBehavior = 'auto'; window.scrollTo(0, 0)")
            page.locator(".skip-link").evaluate("element => element.style.display = 'none'")
            page.screenshot(path=OUTPUT_DIR / filename, full_page=True)
            confirmation_code = "AbCdEfGhIjKlMnOpQrStUv"
            page.goto(f"{BASE_URL}/bluegoldblue/#c={confirmation_code}")
            page.get_by_role("button", name="Confirm BLUE GOLD BLUE updates").wait_for()
            assert page.locator("#bluegold-interest-form").is_hidden()
            assert page.locator("#bluegold-confirm-button").evaluate("element => document.activeElement === element")
            page.get_by_role("button", name="Confirm BLUE GOLD BLUE updates").click()
            page.get_by_text("Your interest is confirmed.", exact=False).wait_for()
            assert confirmed_interest == {"code": confirmation_code}
            assert confirmation_code not in page.url

            page.goto(f"{BASE_URL}/bluegoldblue/#c={confirmation_code}")
            page.get_by_role("button", name="Confirm BLUE GOLD BLUE updates").wait_for()
            page.evaluate("window.location.hash = ''")
            page.locator("#bluegold-interest-form").wait_for(state="visible")
            assert page.locator("#bluegold-confirmation").is_hidden()

            page.goto(f"{BASE_URL}/bluegoldblue/#c=")
            page.get_by_text("That confirmation link is incomplete.", exact=False).wait_for()
            assert page.locator("#bluegold-interest-form").is_visible()
            assert page.locator("#bluegold-confirmation").is_hidden()

            legacy_confirmation = desktop_context.new_page()
            legacy_confirmed = {}

            def capture_legacy_confirmation(route):
                legacy_confirmed.update(json.loads(route.request.post_data))
                route.fulfill(status=200, content_type="application/json", body=json.dumps({"status": "confirmed"}))

            legacy_confirmation.route("https://intentsolutions.io/api/forms/bluegold-confirm", capture_legacy_confirmation)
            legacy_confirmation.goto(f"{BASE_URL}/bluegoldblue/?interest=confirm#token=sealed-bluegold-token")
            legacy_confirmation.get_by_role("button", name="Confirm BLUE GOLD BLUE updates").click()
            legacy_confirmation.get_by_text("Your interest is confirmed.", exact=False).wait_for()
            assert legacy_confirmed == {"token": "sealed-bluegold-token"}
            assert "sealed-bluegold-token" not in legacy_confirmation.url
            legacy_confirmation.close()
        else:
            mobile_interest = page.locator(".bluegold-header .bluegold-interest-link")
            assert mobile_interest.is_visible()
            assert mobile_interest.get_attribute("href") == "#interest"
            page.screenshot(path=OUTPUT_DIR / filename, full_page=True)
        page.close()

    interest_failure = desktop_context.new_page()
    interest_failure.route(
        "https://intentsolutions.io/api/forms/bluegold-interest",
        lambda route: route.fulfill(status=503, content_type="application/json", body=json.dumps({"error": "Interest intake is temporarily unavailable."})),
    )
    interest_failure.goto(f"{BASE_URL}/bluegoldblue/")
    interest_failure.get_by_label("Name Required", exact=True).fill("Jordan Rivera")
    interest_failure.get_by_label("Email Required", exact=True).fill("jordan@example.test")
    interest_failure.get_by_label("Which concept interests you most?").select_option("assisted-migration")
    interest_failure.locator('[name="consent"]').check()
    interest_failure.get_by_role("button", name="Send my confirmation").click()
    interest_failure.get_by_text("Interest intake is temporarily unavailable.", exact=False).wait_for()
    assert "Your information was not added" in interest_failure.locator("#bluegold-form-status").inner_text()
    interest_failure.close()

    incomplete_confirmation = desktop_context.new_page()
    incomplete_confirmation.goto(f"{BASE_URL}/bluegoldblue/?interest=confirm")
    incomplete_confirmation.get_by_text("That confirmation link is incomplete.", exact=False).wait_for()
    assert incomplete_confirmation.locator("#bluegold-interest-form").is_visible()
    incomplete_confirmation.close()

    confirmation_attempts = {"count": 0}
    retry_confirmation = desktop_context.new_page()

    def fail_then_confirm(route):
        confirmation_attempts["count"] += 1
        if confirmation_attempts["count"] == 1:
            route.fulfill(status=503, content_type="application/json", body=json.dumps({"error": "Confirmation is temporarily unavailable."}))
        else:
            route.fulfill(status=200, content_type="application/json", body=json.dumps({"status": "confirmed"}))

    retry_confirmation.route("https://intentsolutions.io/api/forms/bluegold-confirm", fail_then_confirm)
    retry_confirmation.goto(f"{BASE_URL}/bluegoldblue/#c=ZyXwVuTsRqPoNmLkJiHgFe")
    retry_confirmation.get_by_role("button", name="Confirm BLUE GOLD BLUE updates").click()
    retry_confirmation.get_by_text("Confirmation is temporarily unavailable.", exact=False).wait_for()
    retry_button = retry_confirmation.get_by_role("button", name="Try confirmation again")
    assert retry_button.is_visible() and retry_button.is_enabled()
    retry_button.click()
    retry_confirmation.get_by_text("Your interest is confirmed.", exact=False).wait_for()
    assert confirmation_attempts["count"] == 2
    retry_confirmation.close()

    reduced_context = browser.new_context(viewport={"width": 768, "height": 1024}, reduced_motion="reduce")
    reduced_page = reduced_context.new_page()
    reduced_page.goto(f"{BASE_URL}/bluegoldblue/")
    assert reduced_page.evaluate("getComputedStyle(document.documentElement).scrollBehavior") == "auto"
    assert_no_overflow(reduced_page)
    reduced_context.close()

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
        "privacy": "Privacy Policy",
        "app-privacy": "The Beacon Wakes App Privacy Policy",
        "acceptable-use": "Acceptable Use Policy",
        "terms": "Terms and Conditions",
    }
    for route, heading in legal_expectations.items():
        legal = browser.new_page(viewport={"width": 1440, "height": 1000})
        legal.goto(f"{BASE_URL}/{route}/")
        legal.locator(".legal-document h1").wait_for()
        assert heading.casefold() in legal.locator(".legal-document h1").inner_text().casefold()
        rendered = legal.locator(".legal-document").inner_text()
        assert "Intent Solutions LLC" in rendered
        assert "support@intentsolutions.io" in rendered
        assert "No You Pick" not in rendered
        assert "diagnosticpro.reports@gmail.com" not in rendered
        assert "We do not aim any of our products or services directly at children under the age of 13" not in rendered
        assert legal.locator("script, iframe").count() == 0
        assert legal.get_by_role("navigation", name="Legal", exact=True).count() == 1
        assert_no_overflow(legal)
        if route == "privacy":
            legal.evaluate("window.scrollTo(0, 0)")
            legal.screenshot(path=OUTPUT_DIR / "legal-privacy-desktop.png", full_page=True)
        legal.close()

    legal_mobile = browser.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=1)
    legal_mobile.goto(f"{BASE_URL}/acceptable-use/")
    legal_mobile.locator(".legal-document h1").wait_for()
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
