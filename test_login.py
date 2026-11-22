import pytest
from playwright.sync_api import expect


def test_login_page_opens(login_page):
    expect(login_page.page).to_have_title("Swag Labs")
    expect(login_page.login_button).to_be_visible()


def test_login_success(login_page):
    login_page.login("standard_user", "secret_sauce")

    expect(login_page.page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(login_page.page.locator(".title")).to_have_text("Products")


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        (
            "locked_out_user",
            "secret_sauce",
            "Epic sadface: Sorry, this user has been locked out.",
        ),
        ("", "secret_sauce", "Epic sadface: Username is required"),
        ("standard_user", "", "Epic sadface: Password is required"),
        (
            "standard_user",
            "wrong_password",
            "Epic sadface: Username and password do not match any user in this service",
        ),
    ],
)
def test_login_negative(login_page, username, password, expected_error):
    login_page.login(username, password)

    expect(login_page.error).to_be_visible()
    expect(login_page.error).to_have_text(expected_error)
    expect(login_page.page).to_have_url("https://www.saucedemo.com/")
