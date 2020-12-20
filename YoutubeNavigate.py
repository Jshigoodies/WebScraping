from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PATH = "Driver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.youtube.com/")




print("Title: ", driver.title)
#print(driver.page_source)
searchBar = driver.find_element_by_id("search-input")
searchBar.click()

search = driver.find_element_by_name("search_query")

word = input("Put In A Word: ")

search.send_keys(word)
# search.send_keys(Keys.RETURN)  # enter button
driver.find_element_by_id("search-icon-legacy").click()

# So it takes a while for a page to refresh to a new page, so i will add a pause time

time.sleep(3)

main = driver.find_elements_by_class_name("style-scope ytd-video-renderer")
# print(len(main))
length = len(main)
print(length, "Videos \n")

for i in range(length):
    print(i + 1, "\n" + main[i].text + "\n")

heading = input("Copy and Paste the Title Here: ")

link = driver.find_element_by_partial_link_text(heading)
link.click()

'''
# I'll figure this out later
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "video-title"))
    )
    print(main.text)
except:
    driver.quit()
'''

#time.sleep(10) # wait a few seconds
#driver.quit()
# driver.close() closes the current tab