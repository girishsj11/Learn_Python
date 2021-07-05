#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 12:38:35 2020

@author: giri
"""


from selenium import webdriver 
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome("./chromedriver")
url = "http://demo.automationtesting.in/Register.html"

driver.get(url)
sleep(2)

#finding the element by its id called skills
element = driver.find_element_by_id("Skills")

#passing the above elemnt to a Select class to get list of options 
drop_down_options = Select(element)


for _ in drop_down_options.options:
    #listing each element of option
    print(_.text)
 

#selecting one of the skill set among the all options   
drop_down_options.select_by_value("AutoCAD") 
 
sleep(3)
driver.close()




