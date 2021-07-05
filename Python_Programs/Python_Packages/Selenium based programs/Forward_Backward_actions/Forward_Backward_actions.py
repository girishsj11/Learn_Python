# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome("./chromedriver")

driver.maximize_window()

driver.get("https://www.google.com/")

print(driver.title)

driver.find_element_by_name("q").send_keys("Automation testing")
driver.find_element_by_name("q").send_keys(Keys.ENTER)

print(driver.title)

driver.back()

print(driver.title)

driver.forward()

print(driver.title)

driver.close()



