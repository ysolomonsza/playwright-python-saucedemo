from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    print(page.title())
    browser.close()


   # def test_valid_login(page):
   #     page.goto("https://www.saucedemo.com/")
   #     page.fill("#user-name", "standard_user")
   #     page.fill("#password", "secret_sauce")
  #      page.click("#login-button")
   #     assert page.url == "https://www.saucedemo.com/inventory.html"
