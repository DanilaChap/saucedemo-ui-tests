from playwright.sync_api import expect


def test_product_in_cart(inventory_page, cart_page):
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()
    expect(cart_page.get_item("Sauce Labs Backpack")).to_be_visible()


def test_cart_count(cart_page, inventory_page):
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.add_to_cart("Sauce Labs Bike Light")
    inventory_page.open_cart()
    expect(cart_page.cart_items).to_have_count(2)


def test_cart_url(inventory_page, cart_page):
    inventory_page.open_cart()
    expect(cart_page.page).to_have_url("https://www.saucedemo.com/cart.html")
