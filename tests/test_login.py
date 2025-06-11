import pytest
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage

def test_valid_login(page):
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_invalid_login(page):
    login = LoginPage(page)
    login.load()
    login.login("locked_out_user", "wrong_password")
    assert "Epic sadface" in login.get_error_message()
