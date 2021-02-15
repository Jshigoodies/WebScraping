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

# setup
PATH = "Driver\chromedriver.exe"  # might need to edit this pathway for other users than me
driver = webdriver.Chrome(PATH)
driver.get("https://clearcreek.itslearning.com/")
actions = ActionChains(driver)
ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,) #This is a solution that a wished i knew earlier

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


# options method
def options():  # it's basically a list of options that the user can see
    # options

    updates = driver.find_elements_by_tag_name("li")

    string = ""
    for x in updates:
        string = string + x.text + "\n"

    print("\n" + string.strip().replace("\n\n", "\n").replace("\n\n\n\n\n\n\n", "\n"))  # wow this is stupid
    # options (i will later maybe put input)


def CDHome():
    try:
        home = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "l-main-menu-lnk")))
    finally:
        home.click()


def CDCourse():  # i might make another method for inside the course resources
    # courses
    try:
        courses1 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,
                                                                                 '//*[@id="ctl00_CommonMenuRow"]/nav[1]/ul/li[3]')))  # the <li> </li> html link that contains all the properties of courses such as a button and drop down menu
    finally:
        courses1.click()

    try:
        courses2 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_CommonMenuRow"]/nav[1]/ul/li[3]/div/a[2]')))
    finally:
        courses2.click()
    # courses

    # [Navigator/Courses]$

    while True:
        command = input("[Navigator/Courses]$ ")
        cmd = command.split(" ")
        if len(cmd) == 1:
            if cmd[0] == "list":
                string = "Course: "
                try:
                    listCourse1 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_CommonMenuRow"]/nav[1]/ul/li[3]')))

                    listCourse1.click()  # --------------

                    # updates = driver.find_elements_by_tag_name("li")
                    #
                    # string = ""
                    # for x in updates:
                    #     string = string + x.text + "\n"
                    #
                    # print("\n" + string.strip().replace("\n\n", "\n").replace("\n\n\n\n\n\n\n",
                    #                                                           "\n"))  # wow this is stupid
                finally:
                    i = 1
                    while True: # there is an error here that is refusing to return the list of courses. Solution: https://stackoverflow.com/questions/27003423/staleelementreferenceexception-on-python-selenium

                        path = '//*[@id="ctl00_CommonMenuRow"]/nav[1]/ul/li[3]/div/div[4]/ul/li[' + str(i) + ']'  # finding the specific course element
                        find = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_CommonMenuRow"]/nav[1]/ul/li[3]/div/div[4]/ul/li[' + str(i) + ']')))

                        # most stupid alternative, I don't know why it can't print out this one single stupid course

                        actions = ActionChains(driver)
                        actions.move_to_element(find).perform()


                        name = WebDriverWait(driver, 5, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located(
                            (By.XPATH, path)))
                        print("Course " + str(i) + "---------\n" + name.text)


                        i = i + 1

                    # //*[@id="ctl00_CommonMenuRow"]/nav[1]/ul/li[3]/div/div[4]/ul/li[13] <--- 13 is the number of courses I have

                    listCourse1.click()  # ---------------
                # does not work ......
            elif cmd[0] == "back":
                break
            else:
                print(f"\'{command}\' is not recognized as an internal or external command")
        elif len(cmd) == 2:
            if cmd[0] == "click":
                try:
                    listCourse2 = WebDriverWait(driver, 5, ignored_exceptions=ignored_exceptions).until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_CommonMenuRow"]/nav[1]/ul/li[3]')))
                    listCourse2.click()  # clicks the course tab

                    # visibility issue
                    find = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_CommonMenuRow"]/nav[1]/ul/li[3]/div/div[4]/ul/li[' +cmd[1] + ']')))

                    actions = ActionChains(driver)
                    actions.move_to_element(find).perform()

                    courseClick = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_CommonMenuRow"]/nav[1]/ul/li[3]/div/div[4]/ul/li[' +cmd[1] + ']/a')))

                    print(courseClick.text)

                    courseClick.click()

                    intoCourse(cmd[1])  # going into another while loop for the courses inside
                except Exception:
                    print(f"Course # \'{cmd[1]}\' cannot be found")
        else:
            print(f"\'{command}\' is not recognized as an internal or external command")


def intoCourse(num):
    while True:
        command = input("[Navigator/Courses/" + num + "]$ ")
        cmd = command.split(" ")

        if len(cmd) == 1:
            if cmd[0] == "back":
                driver.back()
                break
            else:
                print(f"\'{command}\' is not recognized as an internal or external command")
        elif len(cmd) == 2: # do something with cmd that has the length of 2
            pass
        else:
            print(f"\'{command}\' is not recognized as an internal or external command")


def CDGroups():
    try:
        groups = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_CommonMenuRow"]/nav[1]/ul/li[5]')))
    finally:
        groups.click()
    try:
        groups2 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_CommonMenuRow"]/nav[1]/ul/li[5]/div/a[2]')))
    finally:
        groups2.click()


def CDCalendar():  # this is pointless, i don't even know what the itslearning calandar is for. Obviously not for scheduling.
    try:
        calander1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ctl00_CommonMenuRow"]/nav[1]/ul/li[7]')))
    finally:
        calander1.click()


# ______________________________Where the run actually starts__________________________
# I know, this looks stupid, I'll make it better sometime, it's just dealing with the password and username
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

# navigation like command prompt
while True:
    command = input("[Navigator]$ ")
    cmd = command.split(" ")
    if len(cmd) == 2 and cmd[0] == "cd":
        if cmd[1] == "Courses":
            CDCourse()
            # For all of the CD methods, I should make new commands to navigate through each category. If i don't have time to do all of them, I will at least finish the courses
        elif cmd[1] == "Home":
            CDHome()
        elif cmd[1] == "Groups":
            CDGroups()
        elif cmd[1] == "Calendar":
            CDCalendar()
        else:
            print(f"\'{cmd[1]}\' cannot be found for the path specified.")
    elif len(cmd) == 1 and cmd[0] == "list":
        options()

    # exit cmd
    elif len(cmd) == 1 and cmd[0] == "exit":
        break
    # exit cmd

    else:
        print(f"\'{command}\' is not recognized as an internal or external command")

driver.close()

# list = driver.find_elements_by_tag_name("span")
#
# for x in list:
#     print(x.text)