import unittest
from selenium import webdriver
from Selenium.Tests.signup_test import signup
from Selenium.Tests.product_test import ProductTest
from Selenium.Tests.product_purchase_test import ProductPurchase
from Selenium.Tests import *


class test01(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome('C:/Users/andyb/PycharmProjects/AizonTest/driver/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_start(self):
        driver = self.driver
        driver.get('https://www.demoblaze.com/index.html')
        signup_test = signup(self.driver)
        signup_test.initial_test()
        print("Signup Test done.")
        product_test = ProductTest(self.driver)
        product_test.initial_test()
        print("Product Test done.")
        product_purchase = ProductPurchase(self.driver)
        product_purchase.initial_test()
        print("Product purchase Test done.")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Full Test done.")

    if __name__ == '__main__':
        unittest.main()
