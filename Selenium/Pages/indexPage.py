import time
import datetime
from selenium.webdriver.common.by import By
from Selenium.Reusable_elements.page_locators import Locators


class IndexPage():
    def __init__(self, driver):
        self.driver = driver
        self.user = Locators.user
        self.password = Locators.password
        self.home = Locators.home_xpath
        self.login_complete = Locators.welcome_xpath
        self.cart_tab = Locators.cart_id
        self.signup = Locators.signup_id
        self.login = Locators.login_id
        self.signup_pass = Locators.signup_pass_input_id
        self.login_pass = Locators.signin_pass_input_id
        self.phones_tab = Locators.phone_xpath
        self.laptops_tab = Locators.laptops_xpath
        self.monitors_tab = Locators.monitors_xpath
        self.rand_phone = Locators.rand_phone_xpath
        self.rand_laptop = Locators.rand_laptop_xpath
        self.rand_monitor = Locators.rand_monitor_xpath
        self.signup_user_input = Locators.signup_user_input_id
        self.signup_pass_input = Locators.signup_pass_input_id
        self.signup_button = Locators.signup_button_xpath
        self.signin_user_input = Locators.signin_user_input_id
        self.signin_pass_input = Locators.signin_pass_input_id
        self.signin_button = Locators.signin_button_xpath
        self.logout_button = Locators.logout_id


    def signup_select(self):
        signup = self.driver.find_element(By.ID, self.signup)
        signup.click()
        time.sleep(3)

    def signup_test(self):
        userInput = self.driver.find_element(By.ID, self.signup_user_input)
        dateTimeObj = datetime.datetime.now()
        timestampStr = dateTimeObj.strftime("%Y%m%d_%H%M%S")
        self.user = self.user+timestampStr
        userInput.send_keys(self.user)
        passInput = self.driver.find_element(By.ID, self.signup_pass_input)
        passInput.send_keys(self.password)

    def signup_click(self):
        signup_button = self.driver.find_element(By.XPATH, self.signup_button)
        signup_button.click()
        time.sleep(3)
        self.accept_alert()
        time.sleep(2)

    def login_select(self):
        login = self.driver.find_element(By.ID, self.login)
        login.click()
        time.sleep(3)

    def login_test(self):
        log_user_input = self.driver.find_element(By.ID, self.signin_user_input)
        log_user_input.send_keys(self.user)
        log_pass_input = self.driver.find_element(By.ID, self.signin_pass_input)
        log_pass_input.send_keys(self.password)

    def login_click(self):
        signin_button = self.driver.find_element(By.XPATH, self.signin_button)
        time.sleep(3)
        signin_button.click()
        time.sleep(3)

    def logout_test(self):
        logout = self.driver.find_element(By.ID,self.logout_button)
        time.sleep(3)
        logout.click()

    def go_home(self):
        home = self.driver.find_element(By.XPATH, self.home)
        home.click()

    def phone_test(self):
        phoneTab = self.driver.find_element(By.XPATH,self.phones_tab)
        phoneTab.click()
        randPhone = self.driver.find_element(By.XPATH,self.rand_phone)
        randPhone.click()
        time.sleep(10)

    def laptop_test(self):
        laptopTab = self.driver.find_element(By.XPATH,self.laptops_tab)
        laptopTab.click()
        randLaptop = self.driver.find_element(By.XPATH,self.laptops_tab)
        randLaptop.click()
        time.sleep(10)

    def monitor_test(self):
        monitorTab = self.driver.find_element(By.XPATH, self.monitors_tab)
        monitorTab.click()
        randMonitor = self.driver.find_element(By.XPATH, self.monitors_tab)
        randMonitor.click()
        time.sleep(10)

    def cart_select(self):
        time.sleep(3)
        cart = self.driver.find_element(By.ID, self.cart_tab)
        cart.click()
        time.sleep(2)

    def accept_alert(self):
        obj = self.driver.switch_to.alert
        time.sleep(2)
        obj.accept()
