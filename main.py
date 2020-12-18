from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "Driver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.youtube.com/")


# driver.close() closes the current tab
print(driver.title)

searchBar = driver.find_element_by_id("search-input")
searchBar.click()

search = driver.find_element_by_name("search_query")

search.send_keys("TUYU - I'm getting on the bus to the other world, see ya! MV")
search.send_keys(Keys.RETURN)  # enter button

time.sleep(10)

driver.quit()

# In the html elements, find the id,