import time
from selenium.webdriver.common.by import By
from Selenium.Reusable_elements.page_locators import Locators


class CartPage():
    def __init__(self, driver):
        self.driver = driver
        self.delete_button = Locators.delete_button_xpath
        self.order_button = Locators.order_button_xpath
        self.name_input = Locators.name_input_id
        self.country_input = Locators.country_input_id
        self.city_input = Locators.city_input_id
        self.card_input = Locators.card_input_id
        self.month_input = Locators.month_input_id
        self.year_input = Locators.year_input_id
        self.purchase_button = Locators.purchase_button_xpath
        self.ok_button = Locators.ok_button_xpath

    def delete_product(self):
        delete = self.driver.find_element(By.XPATH, self.delete_button)
        delete.click()

    def order(self):
        time.sleep(3)
        order = self.driver.find_element(By.XPATH, self.order_button)
        order.click()
        time.sleep(3)
        name_input = self.driver.find_element(By.ID, self.name_input)
        name_input.send_keys(Locators.name)
        country_input = self.driver.find_element(By.ID, self.country_input)
        country_input.send_keys(Locators.country)
        city_input = self.driver.find_element(By.ID, self.city_input)
        city_input.send_keys(Locators.city)
        card_input = self.driver.find_element(By.ID, self.card_input)
        card_input.send_keys(Locators.card)
        month_input = self.driver.find_element(By.ID, self.month_input)
        month_input.send_keys(Locators.month)
        year_input = self.driver.find_element(By.ID, self.year_input)
        year_input.send_keys(Locators.year)
        time.sleep(5)

    def purchase_order(self):
        purchase_button = self.driver.find_element(By.XPATH, self.purchase_button)
        purchase_button.click()
        time.sleep(5)

    def confirm_order(self):
        ok_button = self.driver.find_element(By.XPATH, self.ok_button)
        ok_button.click()