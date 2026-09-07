from pathlib import Path

from playwright.sync_api import sync_playwright


BASE_URL = "http://127.0.0.1:4173"
OUTPUT_DIR = Path("/tmp/oma-site-browser")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def assert_page(page, *, mobile: bool = False) -> None:
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    page.locator(".plugin-card").first.wait_for()

    assert page.locator(".plugin-card").count() == 16
    assert "15 official listings" in page.locator("#catalog-summary").inner_text()
    assert page.locator("#plugin-grid").get_attribute("aria-busy") == "false"

    if mobile:
        overflow = page.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth")
        assert not overflow
        page.screenshot(path=OUTPUT_DIR / "mobile.png", full_page=True)
        return

    page.get_by_role("button", name="In review").click()
    assert page.locator(".plugin-card").count() == 1
    assert page.locator(".plugin-card h3").inner_text() == "omaTrail"

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

    social = browser.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=1)
    social.goto(BASE_URL)
    social.wait_for_load_state("networkidle")
    social.evaluate("window.scrollTo(0, 0)")
    social.screenshot(path="site/assets/og-card.png")

    browser.close()

print(f"PASS: browser checks and screenshots written to {OUTPUT_DIR}")
