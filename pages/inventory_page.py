from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.shopping_cart_badge = page.locator(".shopping_cart_badge")
        self.shopping_cart_link = page.locator(".shopping_cart_link")

    def add_to_cart(self, product_name):
        item = self.page.locator(".inventory_item").filter(has_text=product_name)
        item.get_by_role("button", name="Add to cart").click()

    def remove_from_cart(self, product_name):
        item = self.page.locator(".inventory_item").filter(has_text=product_name)
        item.get_by_role("button", name="Remove").click()

    def open_cart(self):
        self.page.locator(".shopping_cart_link").click()
