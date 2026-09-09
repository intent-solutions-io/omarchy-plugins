import json
from pathlib import Path

from playwright.sync_api import sync_playwright


BASE_URL = "http://127.0.0.1:4173"
OUTPUT_DIR = Path("/tmp/oma-site-browser")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
PLUGINS = json.loads((Path(__file__).parents[1] / "site/data/plugins.json").read_text())["plugins"]


def assert_page(page, *, mobile: bool = False) -> None:
    """Verify catalog behavior for a desktop or mobile browser page."""
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    page.locator(".plugin-card").first.wait_for()

    assert "Intent Solutions" in page.locator(".wordmark").inner_text()
    assert "Omarchy Plugins" in page.locator(".wordmark").inner_text()
    assert page.locator(".wordmark-mark").count() == 0
    assert "Omarchy Plugin Works" not in page.locator("body").inner_text()
    assert page.locator(".plugin-card").count() == 16
    assert "16 official listings" in page.locator("#catalog-summary").inner_text()
    assert "no releases waiting on review" in page.locator("#catalog-summary").inner_text()
    assert page.locator("#plugin-grid").get_attribute("aria-busy") == "false"
    assert page.locator('[data-plugin-id="io.github.jeremylongshore.omatrail"] a', has_text="Details").get_attribute("href") == "plugins/omatrail/"
    maintainer_link = page.get_by_role("link", name="Help maintain a plugin")
    assert maintainer_link.count() == 1
    assert "maintainer_interest.md" in maintainer_link.get_attribute("href")

    if mobile:
        overflow = page.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth")
        assert not overflow
        page.screenshot(path=OUTPUT_DIR / "mobile.png", full_page=True)
        return

    page.keyboard.press("/")
    assert page.evaluate("document.activeElement.id") == "plugin-search"
    page.keyboard.press("Escape")

    page.get_by_role("button", name="In review").click()
    assert page.locator(".plugin-card").count() == 0
    assert page.get_by_text("No plugins match those filters.").count() == 1

    page.get_by_role("button", name="All", exact=True).click()
    page.locator("#plugin-search").fill("MLB")
    assert page.locator(".plugin-card").count() == 1
    assert page.locator(".plugin-card h3").inner_text() == "MLB Booth"
    page.locator("#plugin-search").fill("")

    copy_button = page.locator('[data-copy-install="io.github.jeremylongshore.bazaar"]')
    copy_button.click()
    copied = page.evaluate("navigator.clipboard.readText()")
    assert copied == "omarchy plugin add https://github.com/jeremylongshore/omarchy-bazaar-entry.git --enable"

    page.screenshot(path=OUTPUT_DIR / "desktop.png", full_page=True)


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)

    desktop_errors = []
    desktop_context = browser.new_context(
        viewport={"width": 1440, "height": 1000},
        device_scale_factor=1,
        permissions=["clipboard-read", "clipboard-write"],
    )
    desktop = desktop_context.new_page()
    desktop.on("console", lambda message: desktop_errors.append(message.text) if message.type == "error" else None)
    assert_page(desktop)
    assert not desktop_errors, desktop_errors

    mobile_errors = []
    mobile = browser.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=1)
    mobile.on("console", lambda message: mobile_errors.append(message.text) if message.type == "error" else None)
    assert_page(mobile, mobile=True)
    assert not mobile_errors, mobile_errors

    for width, height in ((375, 812), (768, 1024), (1024, 768)):
        responsive_errors = []
        responsive = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=1)
        responsive.on("console", lambda message: responsive_errors.append(message.text) if message.type == "error" else None)
        responsive.goto(BASE_URL)
        responsive.wait_for_load_state("networkidle")
        responsive.locator(".plugin-card").first.wait_for()
        assert responsive.locator(".plugin-card").count() == 16
        assert not responsive.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth")
        assert not responsive_errors, responsive_errors
        responsive.close()

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
        assert detail.get_by_text("Listed", exact=True).count() == 1
        assert detail.locator("[data-detail-copy]").count() == 1
        assert not detail.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth")
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
        assert not mobile.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth")

    failed = desktop_context.new_page()
    failed.route("**/data/plugins.json", lambda route: route.abort())
    failed.goto(BASE_URL)
    failed.wait_for_load_state("networkidle")
    assert failed.get_by_text("The catalog could not load.").count() == 1
    failed.locator("#plugin-search").fill("test")
    assert failed.get_by_text("The catalog could not load.").count() == 1

    browser.close()

print(f"PASS: browser checks and screenshots written to {OUTPUT_DIR}")
