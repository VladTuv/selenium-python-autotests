from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    def _find_element(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"Не удалось найти элемент с локатором: {locator}")

    def _click(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except TimeoutException:
            raise AssertionError(f"Элемент с локатором {locator} не стал кликабельным")

    def _send_keys(self, locator, text):
        element = self._find_element(locator)
        element.clear()
        element.send_keys(text)

    def _get_text(self, locator):
        element = self._find_element(locator)
        return element.text
    
    def _select_by_value(self, locator, value):
        select_element = self._find_element(locator)
        select = Select(select_element)
        select.select_by_value(str(value))

