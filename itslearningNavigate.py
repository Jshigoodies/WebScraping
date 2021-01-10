from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "Driver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# action chain for logging in
# actionClick = ActionChains(driver) # I'll use this later

driver.get("https://clearcreek.itslearning.com/")
print("[Navigator]$", driver.title)

loginButton = driver.find_element_by_id("ctl00_ContentPlaceHolder1_federatedLoginWrapper")
loginButton.click()

driver.implicitly_wait(5)

# username
username = input("[Navigator]$ Please Enter Student Email: ")
try:
    userLoginInput = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "i0116")))
except Exception:
    driver.quit()
userLoginInput.send_keys(username)
userLoginInput.send_keys(Keys.ENTER)

# password
password = input("[Navigator]$ Please Enter Password: ")
try:
    userLoginInputPassword = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "i0118")))
except Exception:
    driver.quit()
userLoginInputPassword.send_keys(password)
userLoginInputPassword.send_keys(Keys.ENTER)

# I really need to implement this code. Right now I'm being so fking lazy about waiting for elements to load,
# but realistically it shouldn't happen,
# but it's not optimized the best way
"""
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "id"))
    )
    print(main.text)
except:
    driver.quit() # probably won't do the quit() method
"""
