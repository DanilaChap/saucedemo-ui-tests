from playwright.sync_api import expect


def test_add_one_product(inventory_page):
    inventory_page.add_to_cart("Sauce Labs Backpack")

    expect(inventory_page.shopping_cart_badge).to_have_text("1")


def test_add_two_products(inventory_page):
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.add_to_cart("Sauce Labs Bike Light")

    expect(inventory_page.shopping_cart_badge).to_have_text("2")


def test_remove_product(inventory_page):
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.remove_from_cart("Sauce Labs Backpack")

    expect(inventory_page.shopping_cart_badge).to_be_hidden()
