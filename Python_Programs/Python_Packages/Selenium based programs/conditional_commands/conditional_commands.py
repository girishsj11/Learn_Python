#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 10:48:24 2020

@author: giri
"""

from selenium import webdriver
from time import sleep


'''
driver.is_enabled() :
    The is enabled action verifies if an element is enabled on the web page and 
    can be executed on all web elements. 
    & returns a boolean value specifying whether the target element is enabled or not displayed on the web page.


driver.is_displayed() :
    The is displayed action verifies if an element is displayed on the web page and 
    can be executed on all web elements. 
    & returns a boolean value specifying whether the target element is displayed or not displayed on the web page.


driver.is_selected() :
    The is_selected action verifies if an element is selected right now on the web page and 
    can be executed only on a radio button, options in select, and checkbox  WebElements. 
    When executed on other elements, it will return false.

'''

driver = webdriver.Chrome("./chromedriver")

url = "http://demo.automationtesting.in/Register.html"

driver.get(url)
driver.maximize_window()
print("Web page title : {} Page".format(driver.title))
sleep(5)

first_name_field = '//input[@placeholder="First Name"]' #input feild where user has to enter some text
gender_field = '//input[@value="Male"]' #where the raido button has to be select from user 

element1 = driver.find_element_by_xpath(first_name_field)

sleep(3)
print("Element is displayed in web page : ",element1.is_displayed()) # which tells us that whether the element is displayed in webpage or hidden 
print("Element is enabled in web page : ",element1.is_enabled()) # which tells us that whether the element is enabled in webpage to enter some text from user

sleep(3)
element2 = driver.find_element_by_xpath(gender_field)
print("Element is selected in web page : ",element2.is_selected()) #which tells us the present radio button is been selected or not . if selected returns True otherwise False

element2.click()
print("Element is selected in web page : ",element2.is_selected()) #after selecting one of gender radio button , should returns True
sleep(5)

driver.close()



