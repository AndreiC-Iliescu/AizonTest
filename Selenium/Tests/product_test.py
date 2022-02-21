import datetime
import time
import unittest

from Selenium.Pages.indexPage import IndexPage
from Selenium.Pages.productPage import ProductPage
from Selenium.Pages.cartPage import CartPage


class ProductTest(unittest.TestCase):

    def __init__(self, driver):
        self.driver = driver

    def initial_test(self):
        index = IndexPage(self.driver)
        productPage = ProductPage(self.driver)
        cartPage = CartPage(self.driver)
        self.generate_screenshot("_IndexPage")
        index.phone_test()
        self.generate_screenshot("_ProductPage")
        productPage.add_product()
        index.cart_select()
        self.generate_screenshot("_CartPage")
        cartPage.delete_product()
        time.sleep(3)
        self.generate_screenshot("_UpdatedCartPage")
        index.go_home()

    def generate_screenshot(self, msg):
        dateTimeObj = datetime.datetime.now()
        timestampStr = dateTimeObj.strftime("%Y%m%d_%H%M%S")
        screenshot_name = "Test Reports/product_test/" + timestampStr + msg + ".png"
        self.driver.save_screenshot(screenshot_name)
        time.sleep(3)
