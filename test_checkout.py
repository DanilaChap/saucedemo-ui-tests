from playwright.sync_api import expect


def test_checkout_success(inventory_page, cart_page, checkout_page):
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()
    cart_page.checkout()
    checkout_page.fill_customer_info("Danila", "Chapurka", "51100")
    checkout_page.finish()

    expect(checkout_page.page).to_have_url(
        "https://www.saucedemo.com/checkout-complete.html"
    )
    expect(checkout_page.complete_header).to_have_text("Thank you for your order!")


def test_checkout_requires_first_name(inventory_page, cart_page, checkout_page):
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()
    cart_page.checkout()
    checkout_page.fill_customer_info("", "Chapurka", "51100")

    expect(checkout_page.error).to_have_text("Error: First Name is required")
    expect(checkout_page.page).to_have_url(
        "https://www.saucedemo.com/checkout-step-one.html"
    )
