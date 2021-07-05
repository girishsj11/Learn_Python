#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 11:13:23 2021

@author: giri
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class Pythonorg(unittest.TestCase):
    
    def setUp(self):
        '''
        
        this method will executes first when ever an instance created for a unittest.Testcase child class
or a main method calls from an unittest class
        '''
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        
    def test_process(self):
        '''
        this method has to be start with keyword test , so that it will call after setup method calls .
it will have important actions to be performed to achieve goal of a program.         
    
        '''
        driver = self.driver
        driver.get("http://www.python.org/")
        self.assertIn("Python", driver.title)
        
        elem = driver.find_element_by_id('id-search-field')
        
        elem.clear()
        
        elem.send_keys('PySimpleGUI')
        
        elem.send_keys(Keys.RETURN)
        
        sleep(4)
        
        self.assertIn("No results found.", driver.page_source)
        
    def tearDown(self):
        '''
        this method calls after all methods calls, its like an destroy method.

        '''
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()
    





