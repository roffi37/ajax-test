from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, value):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((by, value)))
        return element

    def click_element(self, by, value):
        element = self.find_element(by, value)
        element.click()
        return element

    def write_text_to_element(self, by, value, text):
        element = self.click_element(by, value)
        element.send_keys(text)

    def clean_field(self, by, value):
        element = self.click_element(by, value)
        element.clear()
