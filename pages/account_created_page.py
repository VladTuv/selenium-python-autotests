from selenium.webdriver.common.by import By
from pages.base_page import BasePage 

class AccountCreatedPage(BasePage):
    _SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'h2[data-qa="account-created"]')
    _CONTINUE_BUTTON = (By.CSS_SELECTOR, 'a[data-qa="continue-button"]')
    def __init__(self, driver):
     super().__init__(driver)
    def get_success_message_text(self):
     return self._get_text(self._SUCCESS_MESSAGE)
    def click_continue(self):
     self._click(self._CONTINUE_BUTTON)

