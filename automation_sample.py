#python script to search amazon using Safari Web Browser

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

# Searches array
searches = ["27-inch monitors", "LED monitors ASUS", "Blue light protection monitors"]

# Web Driver
driver = webdriver.Safari()

# Amazon
driver.get("https://www.amazon.com")

# Amazon - Search product
search_box = driver.find_element_by_id("twotabsearchtextbox")
search_box.send_keys(random.choice(searches))
find = driver.find_element_by_xpath("//input[@type='submit']")
find.click()
