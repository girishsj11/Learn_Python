#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 20:54:02 2020
@author: giri
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


#setting the options for chrome

opt = Options()
#browser_option.add_argument("--headless")
opt.add_argument("--disable-gpu")
opt.add_argument('--disable-infobars')
#opt.add_argument('--start-fullscreen')
opt.add_argument("--disable-popup-blocking")


#passing the options to chrome to load with arguments
driver = webdriver.Chrome(executable_path="./chromedriver",options=opt)


#passing the options to Firefox to load with arguments
#driver = webdriver.Firefox(options=opt)

#passing the options to Edge to load with arguments
#driver = webdriver.Edge(options=opt)

#passing the options to Opera to load with arguments
#driver = webdriver.Opera(options=opt)


#passing the options to Internet explorer to load with arguments
#driver = webdriver.Ie(options=opt)


#creating url variable with some automation page link 
url = "http://demo.automationtesting.in/Windows.html"

#loading above url onto driver 
driver.get(url)

#printing the title of url
print(driver.title)


#clicking the button to open new window 
click_button = '//a[@href="http://www.selenium.dev"]'
driver.find_element_by_xpath(click_button).click()

#printing the title of url
print(driver.title)

#waiting to get attention 
sleep(5)

if("Yes" == str(input("Do you want to close all windows , please type Yes or No to close only one window : "))):
    #if we use driver.quit() it will closes & deletes the sessions
    driver.quit()

else: 
    #using close method to close older running webapge
    driver.close()
