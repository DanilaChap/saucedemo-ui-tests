from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.get_by_role("button", name="Checkout")

    def get_item(self, product_name):
        item = self.cart_items.filter(has_text=product_name)
        return item

    def checkout(self):
        self.checkout_button.click()
