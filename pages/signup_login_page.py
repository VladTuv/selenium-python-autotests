from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SignupLoginPage(BasePage):
    _NAME_INPUT = (By.CSS_SELECTOR, 'input[data-qa="signup-name"]')
    _EMAIL_INPUT = (By.CSS_SELECTOR, 'input[data-qa="signup-email"]')
    _SIGNUP_BUTTON = (By.CSS_SELECTOR, 'button[data-qa="signup-button"]')

    def __init__(self, driver):
        super().__init__(driver)

    def signup_new_user(self, name, email):
        self._send_keys(self._NAME_INPUT, name)
        self._send_keys(self._EMAIL_INPUT, email)
        self._click(self._SIGNUP_BUTTON)
