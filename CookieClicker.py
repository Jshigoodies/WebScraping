from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

import time

PATH = "Driver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()
driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]  # the upgrades

action = ActionChains(driver)
action.click(cookie)

for i in range(5000):
    action.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_action = ActionChains(driver)
            upgrade_action.move_to_element(item)
            upgrade_action.click()
            upgrade_action.perform()

# A crappy alternative
'''
driver.maximize_window()
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(3)
print(driver.title)

link = driver.find_element_by_id("bigCookie")


while True:
    link.click()
'''