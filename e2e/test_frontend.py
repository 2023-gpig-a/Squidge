from playwright.sync_api import Page, expect


def test_frontend_loads(page: Page):
    page.goto("http://localhost:8080/")
    expect(page.get_by_role("heading", name="Drone Statuses")).to_be_visible()


def test_drone_dispatch(page: Page):
    page.goto("http://localhost:8080/")

    map_el = page.locator('css=.leaflet-container')
    map_position = map_el.bounding_box()
    assert map_position

    # wait for the circle to appear
    page.get_by_role("button", name="Direct Drones").click()

    with page.expect_response("http://localhost:8082/drone_dispatch/circle") as dispatch_res:
        expect(page.locator("css=.leaflet-interactive")).to_be_attached()
        # TODO: Not sure why this needs to be clicked multiple times - test-only issue
        page.mouse.click(map_position['x'] + (map_position["width"]/10), map_position['y'] + (map_position["height"]/10), delay=100)
        page.mouse.click(map_position['x'] + (map_position["width"]/10), map_position['y'] + (map_position["height"]/10), delay=100)
        page.mouse.click(map_position['x'] + (map_position["width"]/10), map_position['y'] + (map_position["height"]/10), delay=100)
    response = dispatch_res.value
    assert response.status == 200
