#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 20:45:49 2021

@author: giri
"""

############################################

#Alert popu window handling

############################################


from selenium import webdriver

url = "http://demo.guru99.com/test/delete_customer.php"

driver = webdriver.Chrome('./chromedriver')

driver.get(url)

element = driver.find_element_by_xpath('//input[@name="cusid"]')

element.clear()

element.send_keys('1234')

submit = driver.find_element_by_xpath('//input[@name="submit"]')

submit.click()

alert = driver.switch_to.alert

print(alert.text)

alert.accept()

driver.close()

############################################

#Handling multiple windows which were opened in browser

############################################

from selenium import webdriver
from time import sleep

url = "http://demo.guru99.com/popup.php"

driver = webdriver.Chrome('./chromedriver')

driver.get(url)

#driver.maximize_window()

#print(driver.current_window_handle)

driver.find_element_by_xpath("//a[contains(@href,'popup.php')]").click()

mainwindow = driver.window_handles

ch_wnd = mainwindow[1]

pa_wnd = mainwindow[0]
#print(driver.current_window_handle)

print(len(mainwindow))

for _ in range(5):
    driver.switch_to_window(pa_wnd)
    #driver.switch_to.window(pa_wnd)
    sleep(2)
    driver.switch_to_window(ch_wnd)
    #driver.switch_to.window(ch_wnd)
    sleep(2)

driver.quit()

############################################

#Handling & getting the content/text from the table on webpage

############################################

from selenium import webdriver

url = 'http://demo.guru99.com/test/write-xpath-table.html' 

driver = webdriver.Chrome('./chromedriver')

print("Browser used :",driver.desired_capabilities['browserName'])

print("Browser version :",driver.desired_capabilities['browserVersion'])

print("On platofrm :",driver.desired_capabilities['platformName'])

driver.get(url)

elements = driver.find_elements_by_xpath('//tbody/tr/td')

print("Table contents are : \n")

for _ in range(len(elements)):
    print(elements[_].text)
    
driver.close()



##############################################

#Clicking on image & finding its locator by css class selector

#############################################


from selenium import webdriver

url = "https://www.facebook.com/login/identify?ctx=recover"

driver = webdriver.Chrome('./chromedriver')

driver.get(url)

driver.find_element_by_css_selector('a[title="Go to Facebook home"]').click()

#print(driver.title)

if (driver.title == "Facebook – log in or sign up"):
    print("True")
else:
    print("False")
    
driver.quit()


##############################################

#Clicking & finding the locator by css class selector by an id of an element as a parameter

#############################################


from selenium import webdriver
from time import sleep

url = 'https://www.facebook.com/' 

driver = webdriver.Chrome('./chromedriver')

driver.get(url)

email = driver.find_element_by_css_selector('#email')

email.click()

email.send_keys('1234@gmail.com')

sleep(2)

driver.close()



#################################################

#Finding the element by its linktext & clicking on it

#################################################

from selenium import webdriver

url = "http://demo.guru99.com/test/link.html"

driver = webdriver.Chrome('./chromedriver')

driver.get(url)

#driver.find_element_by_link_text('click here').click()

elements = driver.find_elements_by_link_text('click here')

#print(len(elements))

#elements[0].click()
elements[1].click()
print(driver.title)
    
driver.close()


################################################

#Finding the element by its partial linktext & clicking on it

################################################

from selenium import webdriver

url = "http://demo.guru99.com/test/link.html"

driver = webdriver.Chrome('./chromedriver')

driver.get(url)

elements = driver.find_elements_by_partial_link_text('here')

#print(len(elements))

#elements[0].click()
elements[1].click()
print(driver.title)
    
driver.close()


###############################################

#Finding the element by its linktext & clicking on it with help of ActionChain class

###############################################

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

url = "http://demo.guru99.com/test/link.html"

driver = webdriver.Chrome('./chromedriver')
action = ActionChains(driver)

driver.get(url)


#driver.find_element_by_link_text('click here').click()

elements = driver.find_elements_by_link_text('click here')

#action = ActionChains(driver)

action.click(elements[0]).perform()

print(driver.title)

driver.quit()


###############################################

#different actions on single element by using action chains class

###############################################

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

url = "https://www.facebook.com/login/identify?ctx=recover"

driver = webdriver.Chrome('./chromedriver')

driver.get(url)

element = driver.find_element_by_id("identify_email")

actions = ActionChains(driver)

actions.click(element).send_keys('12345').double_click(element).context_click(element).perform()
sleep(4)

driver.quit()



###############################################

#adding coockies to webpage by using firefox in linux machine

###############################################

from selenium import webdriver
from time import sleep

  
# create webdriver object 
driver = webdriver.Firefox(executable_path='./geckodriver')
  
# get geeksforgeeks.org 
driver.get("https://www.google.com/") 
  
# add_cookie method driver 
print("\nBefore adding user defined cookie : ",driver.get_cookies())
driver.add_cookie({"name" : "Function_name", "value" : "Function_value"}) 
print("\nAfter adding user defined cookie : ",driver.get_cookies())

sleep(5)

print("\nDriver title : ",driver.title)

driver.close()


###############################################

#finding size & its loaction of an element located 

###############################################

from selenium import webdriver

# create webdriver object 
driver = webdriver.Firefox(executable_path='./geckodriver')
  
# get geeksforgeeks.org 
driver.get("https://www.google.com/") 
  
element = driver.find_element_by_name("q")

print("\nx & Y co-ordination values : ",element.location)
print("\nSize of an element in webpage : ",element.size)
print("or")
print(element.rect)

driver.close()
