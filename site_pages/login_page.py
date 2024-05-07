from site_pages.base_page import BasePage
from playwright.sync_api import Page

class LoginPage(BasePage):
    def __init__(self, page: Page):
        self.page = page

    # User flow
    def login_user(self, username, password):
        self.page.locator("#user-name").fill(username)
        self.page.locator("#password").fill(password)
        self.page.locator("#login-button").click()

    # Locators
    def login_error_message(self):
        self.page.locator("#login_button_container > div > form > h3")