from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    _SIGNUP_LOGIN_BUTTON = (By.CSS_SELECTOR, 'a[href="/login"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://automationexercise.com/"

    def open(self):
        self.driver.get(self.url)

    def go_to_login_page(self):
        self._click(self._SIGNUP_LOGIN_BUTTON)
