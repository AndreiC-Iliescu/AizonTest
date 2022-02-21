import time
from selenium.webdriver.common.by import By
from Selenium.Reusable_elements.page_locators import Locators


class ProductPage():
    def __init__(self, driver):
        self.driver = driver
        self.add_button = Locators.add_button_xpath

    def add_product(self):
        add = self.driver.find_element(By.XPATH, self.add_button)
        add.click()
        time.sleep(10)
        self.accept_alert()

    def accept_alert(self):
        obj = self.driver.switch_to.alert
        time.sleep(2)
        obj.accept()
