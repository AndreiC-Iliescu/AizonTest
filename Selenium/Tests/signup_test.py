import datetime
import time
import unittest
from Selenium.Pages.indexPage import IndexPage
from selenium.webdriver import Chrome


class signup(unittest.TestCase):
    def __init__(self, driver):
        self.driver = driver

    def initial_test(self):
        time.sleep(2)
        self.generate_screenshot("_IndexPage")
        page = IndexPage(self.driver)
        page.signup_select()
        page.signup_test()
        self.generate_screenshot("_SignUpTab")
        page.signup_click()
        self.generate_screenshot("_SignUpComplete")
        page.login_select()
        print("Sign up complete.")
        self.generate_screenshot("_LogInTab")
        page.login_test()
        self.generate_screenshot("_LogInTab")
        page.login_click()
        self.generate_screenshot("_LogInComplete")
        page.logout_test()
        print("Login complete.")
        self.generate_screenshot("_LogOutComplete")

    def generate_screenshot(self,msg):
        dateTimeObj = datetime.datetime.now()
        timestampStr = dateTimeObj.strftime("%Y%m%d_%H%M%S")
        screenshot_name = "Test Reports/signup_test/"+timestampStr+msg+".png"
        self.driver.save_screenshot(screenshot_name)
        time.sleep(3)
