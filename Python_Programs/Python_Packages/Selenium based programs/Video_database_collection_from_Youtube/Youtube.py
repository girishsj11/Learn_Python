# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 21:06:59 2020

@author: giri
"""


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
import time
import mouse_operations
import configparser
import sqlite3





# initializing logging file
logging.basicConfig(format='%(asctime)s: %(levelname)s:%(message)s', filename='youtube.log', level=logging.INFO)
    
### Calling property file ####
    
config = configparser.RawConfigParser()
config.read('youtube.properties')
    
# setting options for chrome driver
browser_option = Options()
#browser_option.add_argument("--headless")
browser_option.add_argument("--disable-gpu")
browser_option.add_argument('--disable-infobars')
browser_option.add_argument('--start-fullscreen')
browser_option.add_argument("--disable-popup-blocking")
    
#setting up a chrome webbrowser with its driver
driver = webdriver.Chrome(executable_path='./chromedriver.exe',options=browser_option)











###########   SQL Class data base code to store a video title & its duration onto a database.db file 



class Database_sql:

    def __init__(self):
        #Creating data base file for storing youtube vidoes names & duration
        self.sql_file = sqlite3.connect('YouTube.db')
        #c=conn.cursor()

#Creating a table called Youtube for storing values in an order    
    def creation_databse(self):
        pointer = self.sql_file.cursor()
        #pointer.execute('CREATE TABLE IF NOT EXISTS Youtube_Python_Videos(Video_Name TEXT,Duration REAL,Channel_Name TEXT)')
        pointer.execute('CREATE TABLE IF NOT EXISTS Youtube_Video_Table(Video_Name TEXT,Duration REAL)')
        pointer.close()
        
 
#to find out the video duration
    def Duration_calculation(self,video_content):
        if(video_content.__contains__('ago')):
            try:
                duration = video_content.split("ago")
                hrs="hours"
                sec="seconds"
                mnts="minutes"   
                
                
                if(duration[1].count(sec)>=1):
                    value = duration[1].split(sec)
                    return (value[0]+sec)
                
                else:
                    if(duration[1].count(mnts)>=1):
                        value = duration[1].split(mnts)
                        return (value[0]+mnts)
                    elif(duration[1].count(hrs)>=1):
                        value = duration[1].split(hrs)
                        return (value[0]+hrs)
                
                
                
            except:
                return 0
                
        else:
            return 0
            
 
        
 
#After search result, now we need to get the all video titels & its duration
    def filling_data_to_sqlFile(self):
        pointer = self.sql_file.cursor()
        final_count = int(input("Enter the end count value to store video tutorials onto the database file : "))
        
        time.sleep(3)
        for itr in range(1,final_count+1):
            if(itr==15):
                mouse_operations.scroll_down(driver)
            
            videos_details = (config.get('xpath', 'single_videos_xpath'))+str([itr])
            
            time.sleep(1)
            video_title = mouse_operations.GetAttribute(driver,videos_details,"title")
            time.sleep(1)
            video_content = mouse_operations.GetAttribute(driver,videos_details,"aria-label")
            
            video_duration = Database_sql.Duration_calculation(self,video_content)
            
            if(video_title==None):
                continue
            else:
                entry = 'INSERT INTO Youtube_Video_Table VALUES("{}","{}")'.format(video_title,video_duration)
                pointer.execute(entry)
                self.sql_file.commit()
                
        pointer.close()







def Menu():
    
    def info(msg1='',msg2='',msg3=''):
        logging.info(str(msg1)+str(msg2)+str(msg3))
        print(msg1,msg2,msg3)
    
    
    
    #opening youtube in webbrowser
    info("<YouTube>  trying to connecting to url", ' at ',time.ctime())
    driver.get(config.get('url', 'url'))
    time.sleep(2)
    
    #sending the data as "python tuutorial" to search results in youtube and hitting enter
    mouse_operations.MouseClickandSendKeysEnter(driver,config.get('xpath', 'search_bar'),config.get('data','requirement'))

    #Object for sql_databse class to store the value of video title & its duration onto a file
    obj = Database_sql()
    obj.creation_databse()
    obj.filling_data_to_sqlFile()





if __name__ == "__main__":
    Menu()
    print("Database is updated successfully !!!")
    driver.quit()

            
                
            


