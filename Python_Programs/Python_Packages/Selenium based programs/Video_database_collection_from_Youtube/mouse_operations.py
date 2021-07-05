# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 20:00:35 2020

@author: giri
"""

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
import logging
import time

'''
---------------------------------------------------------------------------
Logger 
formate:- '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
---------------------------------------------------------------------------
'''
#log_file_name = (str(input("Provide us the name to store mouse operation logs as readable formate : ")))+'.log'

log_file_name = 'mouse_operations.log'


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
timestr = time.strftime("%Y%m%d-%H%M%S")
handler = logging.FileHandler(log_file_name)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


'''
---------------------------------------------------------------------------
Logging Initializer
---------------------------------------------------------------------------
'''
def PopUpAlert(driver):
    try:
        obj = driver.switch_to.alert
        print("Please wait for few more days to handle all your PopUp alert methods by code")
    except Exception as timeout:
        message = "We are in foundation of the program building , in future will add up a function which handle your popup alerts"
        #logger.info("{} - {} - {} ".format(message,obj.text,timeout))
        logger.info('%s - %s - %s', message,obj.text,timeout)
        
        
def MoveToElement(driver,xpath):
    try:
        element = driver.find_element_by_xpath(xpath)
        sleep(1)
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()
    except Exception as timeout:
        logger.info('%s - %s - %s', "Unable to find the Xpath element  ",xpath,timeout)
        
        
def GetAttribute(driver,xpath,string):
    try:
        element = driver.find_element_by_xpath(xpath)
        sleep(1)
        value = element.get_attribute(string)
        return value
    except Exception as timeout:
        logger.info('%s - %s - %s', "Unable to find the Xpath element ",xpath,timeout)
        
        
def LoadPage(driver,xpath,timeout):
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH,xpath)))
        print("The Page is loaded successfully !!! ")
        
    except Exception as timeout:
        logger.info('%s - %s - %s', "Unable to find the Xpath  ",xpath,timeout)
        

def MouseClick(driver,xpath):
    try:
        element = driver.find_element_by_xpath(xpath)
        sleep(1)
        actions = ActionChains(driver)
        actions.click(element).perform()
    except Exception as timeout:
        logger.info('%s - %s - %s', "Unable to find the Xpath  ",xpath,timeout)
        
        
        
def Clear(driver, xpath):
    try:
        element = driver.find_element_by_xpath(xpath)
        actions = ActionChains(driver)
        actions.click(element).perform()
        element.clear()
    except Exception as timeout:
        logger.info('%s - %s - %s', "Unable to find the Xpath  ",xpath,timeout)
        
        
def MouseClickAndSendKeys(driver,xpath,value):
    try:
        Clear(driver, xpath)
        MouseClick(driver,xpath)
        actions = ActionChains(driver)
        actions.send_keys(value).perform()
    except Exception as timeout:
        logger.info('%s - %s - %s', "Unable to find the Xpath  ",xpath,timeout)  
        
        
def MouseClickandSendKeysEnter(driver,xpath,value):
    try:
        MouseClickAndSendKeys(driver,xpath,value)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER).perform()
    except Exception as timeout:
        logger.info('%s - %s - %s', "Unable to find the Xpath  ",xpath,timeout) 
        
    
def MouseClickandSendKeysTab(driver,xpath,value):
    try:
        MouseClickAndSendKeys(driver,xpath,value)
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB).perform()
    except Exception as timeout:
        logger.info('%s - %s - %s', "Unable to find the Xpath  ",xpath,timeout) 
        
        

def readText(driver,xpath):
    try:
        element = driver.find_element_by_xpath(xpath)
        return element.text
    except Exception as timeout:
        logger.info('%s - %s - %s', "Unable to find the Xpath  ",xpath,timeout)
        
        
        
def Double_Click(driver,xpath):
    try:
        element = driver.find_element_by_xpath(xpath)
        actions = ActionChains(driver)
        actions.double_click(element)
        actions.perform()
    except Exception as timeout:
        logger.info('%s - %s - %s', "Unable to find the Xpath  ",xpath,timeout)
        
        
def Dropdown_Options(driver,xpath):
    try:
        element = driver.find_element_by_xpath(xpath)
        all_options = Select(element)
        return all_options
    except Exception as timeout:
        logger.info('%s - %s - %s', "Unable to find the Xpath  ",xpath,timeout)
        
        
        
   
def scroll_down(driver):
    try:
        driver.execute_script("window.scrollTo(0, 5500);")
    except Exception as timeout:
        logger.info('%s - %s - %s', "Unable to find the Xpath  ","and to scroll",timeout)
        
    
        
        
        
        
        



























