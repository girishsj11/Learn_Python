# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 20:08:58 2020

@author: giri
"""

from selenium.webdriver.support.select import Select
from selenium import webdriver

url = "https://www.onlinedataentryjob.com/form-filling-work.php"

driver = webdriver.Chrome('chromedriver.exe')

driver.get(url)



#"//select[@name='insurance[1532]']"
i=1532
beforexpath = "insurance["+str(i)+"]"

options = Select(driver.find_element_by_name(beforexpath))


all = options.options
for i in range(1,len(all)):
    print(all[i].text)
    
#options.select_by_value('Yes')
    
    

