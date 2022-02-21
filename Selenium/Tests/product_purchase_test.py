import datetime
import time
import unittest

from Selenium.Pages.indexPage import IndexPage
from Selenium.Pages.productPage import ProductPage
from Selenium.Pages.cartPage import CartPage


class ProductPurchase(unittest.TestCase):

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
        cartPage.order()
        time.sleep(3)
        self.generate_screenshot("_OrderTab")
        time.sleep(4)
        cartPage.purchase_order()
        self.generate_screenshot("_OrderConfirmed")
        time.sleep(4)
        cartPage.confirm_order()
        time.sleep(5)

    def generate_screenshot(self, msg):
        dateTimeObj = datetime.datetime.now()
        timestampStr = dateTimeObj.strftime("%Y%m%d_%H%M%S")
        screenshot_name = "Test Reports/product_purchase_test/" + timestampStr + msg + ".png"
        self.driver.save_screenshot(screenshot_name)
        time.sleep(3)
