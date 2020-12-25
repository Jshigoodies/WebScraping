from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

import time

PATH = "Driver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

action = ActionChains(driver)
'''
driver.maximize_window()
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(3)
print(driver.title)

link = driver.find_element_by_id("bigCookie")


while True:
    link.click()
'''