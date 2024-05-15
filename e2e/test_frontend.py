from playwright.sync_api import Page, expect


def test_frontend_loads(page: Page):
    page.goto("http://localhost:8080/")
    expect(page.get_by_role("heading", name="Drone Statuses")).to_be_visible()
