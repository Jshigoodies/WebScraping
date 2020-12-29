import unittest
from selenium import webdriver
import page

PATH = "Driver\chromedriver.exe"


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("https://www.python.org/")