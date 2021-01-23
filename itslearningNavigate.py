from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

# setup
PATH = "Driver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://clearcreek.itslearning.com/")


# login
def start():
    # action chain for logging in
    # actionClick = ActionChains(driver) # I'll use this later
    print("[Navigator]$", driver.title.upper())

    loginButton = driver.find_element_by_id("ctl00_ContentPlaceHolder1_federatedLoginWrapper")
    loginButton.click()


# username
def userMethod():
    username = input("[Navigator]$ Please Enter Student ID: ")
    username = username + "@ccisd.net"
    try:
        userLoginInput = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "i0116")))
    finally:
        userLoginInput.send_keys(username)
        userLoginInput.send_keys(Keys.ENTER)

    try:
        Error = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "usernameError")))
        print("[Navigator]$ Email Does not Exist")
        userLoginInput.clear()
        return True
    except Exception:
        return False


# password
def passWordMethod():
    password = input("[Navigator]$ Please Enter Password: ")
    try:
        userLoginInputPassword = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "i0118")))
    finally:
        userLoginInputPassword.send_keys(password)
        userLoginInputPassword.send_keys(Keys.ENTER)

    try:
        Error = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "passwordError")))
        print("[Navigator]$ Password Or Email is Wrong \n[Navigator]$ Restarting...")
        return True
    except Exception:
        return False


# I know, this looks stupid, I'll make it better sometime
loop = True
loop2 = True
loop3 = True

start()
while loop:
    while loop2:
        if not userMethod():
            loop2 = False
    while loop3:
        if not passWordMethod():
            loop3 = False
        else:
            driver.back()
            driver.back()
            break
    loop = loop3
    loop2 = loop3

print("[Navigator]$ Login Successful")

# list = driver.find_elements_by_tag_name("span")
#
# for x in list:
#     print(x.text)

