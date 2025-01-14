from site_pages.base_page import BasePage
from playwright.sync_api import Page, expect

class LoginPage(BasePage):
    def __init__(self, page: Page):
        self.page = page

    # login user flow
    def login_user(self, username, password):
        self.page.locator("#user-name").fill(username)
        self.page.locator("#password").fill(password)
        self.page.locator("#login-button").click()

    # getting Locators    
    def login_page_title(self):
        return self.page.title()

    def login_page_textfields(self):
        self.page.locator("#login_button_container")