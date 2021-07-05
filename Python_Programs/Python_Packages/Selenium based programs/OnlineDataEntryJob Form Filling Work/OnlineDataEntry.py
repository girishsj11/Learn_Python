# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 18:48:06 2020

@author: giri
"""

import mouse_operations
from selenium import webdriver
import configparser
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

### Calling property file ####
    
config = configparser.RawConfigParser()
config.read('OnlineDataEntry.properties')

# setting options for chrome driver
browser_option = Options()
#browser_option.add_argument("--headless")
browser_option.add_argument("--disable-gpu")
browser_option.add_argument('--disable-infobars')
#browser_option.add_argument('--start-fullscreen')
browser_option.add_argument("--disable-popup-blocking")
    
#setting up a chrome webbrowser with its driver
driver = webdriver.Chrome(executable_path='C:/Users/giri/.spyder-py3/Python_Programs/OnlineDataEntry/chromedriver.exe',options=browser_option)

#loading the login page of onlinedata entry
driver.get(config.get('url','login_url'))
sleep(5)

#entering username onto the login webpage
mouse_operations.MouseClickAndSendKeys(driver,config.get('xpath','username'),config.get('data','username'))
sleep(2)

#entering password onto the login webpage
mouse_operations.MouseClickAndSendKeys(driver,config.get('xpath','password'),config.get('data','password'))
sleep(2)


#pressing the login button after entering username & password 
mouse_operations.MouseClick(driver,config.get('xpath','signin'))
sleep(2)



#After successfull login 
#we are moving to earn money tab & selecting form filling work
mouse_operations.MouseClick(driver,config.get('xpath','EarnMoney_Tab'))
sleep(3)

#Entering to form filling work area with help of xpath
mouse_operations.MouseClick(driver,config.get('xpath','FormFilling_Work'))
sleep(2)


Row_Counts = len(driver.find_elements_by_xpath(config.get('xpath','Total_Row_Count')))
print("\nTotal Row count is : ",Row_Counts)

Column_Counts = len(driver.find_elements_by_xpath(config.get('xpath','Total_Column_Count')))
print("\nTotal Column count is : ",Column_Counts)


before_XPath = "//*[@id='table_data']/tbody/tr["
aftertd_XPath = "]/td["
aftertr_XPath = "]"
Table_Data = list()

print()

#printing the data of the table 

for row in range(1,(Row_Counts+1)):
    
    for column in range(2,(Column_Counts+1)):
        FinalXPath = before_XPath + str(row) + aftertd_XPath + str(column) + aftertr_XPath
        cell_text = driver.find_element_by_xpath(FinalXPath).text
        #print(cell_text)
        if(cell_text=="Yes" or cell_text=="No"):
            continue
        else:
            Table_Data.append(cell_text)
        
     
    
    
#print(Table_Data)
'''
        for entry in range(1,Row_Counts):
            Table_entry = config.get('xpath','Table_Entry')+'['+str(entry)+']'
            mouse_operations.MouseClickAndSendKeys(driver,Table_entry,cell_text)
'''
     
for i in range(1,Row_Counts*Column_Counts+1):
    if(i%7==0):
        Table_entry = config.get('xpath','Table_Entry')+'['+str(i)+']'
        mouse_operations.MouseClickAndSendKeys(driver,Table_entry,Table_Data[i-1])
        sleep(10)
        print("Waiting for user to select the proper option !!")
            #clicking the next button after all entry
        mouse_operations.MouseClick(driver,config.get('xpath','Next_Button'))
    '''        
    if(i%8==0):
        Table_entry = config.get('xpath','Table_Entry')+'['+str(i+1)+']'
        mouse_operations.MouseClickAndSendKeys(driver,Table_entry,Table_Data[i+1])
    '''
        
    
    Table_entry = config.get('xpath','Table_Entry')+'['+str(i)+']'
    mouse_operations.MouseClickAndSendKeys(driver,Table_entry,Table_Data[i-1])
        
    '''
        if(cell_text=='No'):
            insurance = driver.find_element_by_xpath(config.get('xpath','Table_Entry_Insurance'))
            options = Select(insurance)
            options.select_by_value(cell_text)
        else:
            insurance = driver.find_element_by_xpath(config.get('xpath','Table_Entry_Insurance'))
            options = Select(insurance)
            options.select_by_value(cell_text)
            
    '''  
        #clicking the next button after all entry


#driver.quit()


