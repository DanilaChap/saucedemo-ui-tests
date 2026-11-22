import pytest
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.fixture
def login_page(page):
    login = LoginPage(page)
    login.open()
    return login


@pytest.fixture
def inventory_page(login_page, page):
    login_page.login("standard_user", "secret_sauce")
    return InventoryPage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)
