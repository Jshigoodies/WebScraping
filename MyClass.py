from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException

class Log:
    # login
    def __init__(self, _driver):
        self.driver = _driver

    def start(self):
        # action chain for logging in
        # actionClick = ActionChains(driver) # I'll use this later
        print("[Navigator]$", self.driver.title.upper())

        loginButton = self.driver.find_element_by_id("ctl00_ContentPlaceHolder1_federatedLoginWrapper")
        loginButton.click()

    # username
    def userMethod(self):
        username = input("[Navigator]$ Please Enter Student ID: ")
        username = username + "@ccisd.net"
        try:
            userLoginInput = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "i0116")))
        finally:
            userLoginInput.send_keys(username)
            userLoginInput.send_keys(Keys.ENTER)

        try:
            Error = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "usernameError")))
            print("[Navigator]$ Email Does not Exist")
            userLoginInput.clear()
            return True
        except Exception:
            return False

    # password
    def passWordMethod(self):
        password = input("[Navigator]$ Please Enter Password: ")
        try:
            userLoginInputPassword = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "i0118")))
        finally:
            userLoginInputPassword.send_keys(password)
            userLoginInputPassword.send_keys(Keys.ENTER)

        try:
            Error = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "passwordError")))
            print("[Navigator]$ Password Or Email is Wrong \n[Navigator]$ Restarting...")
            return True
        except Exception:
            return False
