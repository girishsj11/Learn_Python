# Selenium 

*Selenium is a free/open-source automated testing framework to validate a web applications across the different browsers & platofrms. we can create a selenium test code with help of any scripting langauage like python,java, C#,ruby etc...*
  
  **List of tools:**
  
  1. Selenium Integrated Development Environment (IDE)
  2. Selenium Remote Control (RC)
  3. WebDriver
  4. Selenium Grid
  
  ![Selenium_Tools](https://www.guru99.com/images/SeleniumSuite.png)


  **Types of Selenium Waits For Page Load:**
  
  1. Thread.Sleep() method
  2. Implicit Wait
  3. Explicit Wait
  4. Fluent Wait
  
     1. *Thread.sleep() :*
     
      Sleep is a static method that belongs to the thread class. This method can be called using the reference of the class name i.e Thread. If you use Thread.sleep while performing automation testing with Selenium, then this method will stop the execution of the script for the specified duration of time, irrespective of whether the element is found or not on the web page. It accepts the time duration in milliseconds. The syntax for the same is:

            Thread.sleep(3000);
         
     - Selenium Webdriver waits for the specified time, irrespective of the element is found or not. In case the element is found much before the specified duration, the script will still wait for the time duration to elapse, thereby increasing the execution time of the script.
     
     - If the element to be present does not appear after a static time and keep changing, then you will never know an estimated time needed for the sleep function. In case it takes more time than the defined time, the script shall throw an error. 
     
     - Thread.sleep is intended only for the element it is written prior to. In case you have two to fours elements which need to wait for a certain duration to load, you need to specify Thread.sleep as many times in that case.

     2. *Implicit Wait() :*
     
      - Implicit wait which allows you to halt the WebDriver for a particular period of time until the WebDriver locates a desired element on the web page.
      
      - It does not wait for the complete duration of time. In case it finds the element before the duration specified, it moves on to the next line of code execution, thereby reducing the time of script execution. This is why Implicit wait is also referred to as dynamic wait. If it does not find the element in the specified duration, it throws ElementNotVisibleException.
      
            driver.manage().timeouts().implicitlyWait(Time Interval to wait for, TimeUnit.SECONDS);
            
            or
            
            from selenium import webdriver
            driver = webdriver.Firefox()
            driver.implicitly_wait(10) # seconds
            driver.get("http://somedomain/url_that_delays_loading")
            myDynamicElement = driver.find_element_by_id("myDynamicElement")
            
     3. *Explicit Wait() :*
     
      - An explicit wait is a code you define to wait for a certain condition to occur before proceeding further in the code. The extreme case of this is time.sleep(), which sets the condition to an exact time period to wait. There are some convenience methods provided that help you write code that will wait only as long as required. WebDriverWait in combination with ExpectedCondition is one way this can be accomplished.
      
            from selenium.webdriver.support import expected_conditions as EC
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.element_to_be_clickable((By.ID, 'someid')))

     4. *Fluent wait() :*

      - The Fluent Wait command defines the maximum amount of time for Selenium WebDriver to wait for a certain condition to appear. It also defines the frequency with which WebDriver will check if the condition appears before throwing the “ElementNotVisibleException”.


## ***Video_database_collection_from_Youtube_using-Selenium-Python***

* Prerequisite package installation :
  - pip install db-sqlite3
  - pip install configparser
  - pip install logging
  - pip install selenium
    
       
 * Prerequisite program code :  mouse_operations.py
   - file contains all type of operations which human will do on web pages, so whenever its required we can specific operation/action based on requirement in our main program.
   - actions/operations/user_functions are listed below -->
     1. MoveToElement :- which moves the control to specific xpath 
     2. GetAttribute  :- which returns the attribute(either href,text,html link,name) based on input string value to the function
     3. LoadPage :- which waits the webpage to load a specific content/xpath to be present on the loaded webpage content.
     4. MouseClick :- which performs click operation on the specific element/xpath.
     5. Clear :- which performs clear operation on the specifc element.
     6. MouseClickAndSendKeys :- which performs click,clear operations then it will sends the given value on function to the element.
     7. MouseClickandSendKeysEnter :- which does the operation of MouseClickAndSendKeys, then hits the enter key.
     8. Dropdown_Options :- which will returns the all listed options on the particular xpath/element.
     9. scroll_down :- which scrolls down the webpage content by a mentioned offset value .
   
   
* Prerequisite property file : youtube.properties
  - file contains useful & input commands to the main program code , which contains the xpath address on it and also user can change the requirement based on his/her interest.
  
  
* Main program code : Youtube.py
  - This is the our main program file , which divides the whole actions into subparts as listed below :
      1. creating one log file to store the operations/errors occured on main program code validation 
      2. adding the few option settings to Chrome browser .
      3. opening web browser with 'requirement' data from 'youtube.properties' file on youtube 
      4. creating sql_databse class to store all video titels & its duration on to the file .
      5. once execution is done user can check the 'Youtube.db' file which generates & stored on the same directory .



## ***OnlineDataEntryJob Form Filling Work-Selenium-Python***

* Prerequisite package installation :
  - pip install configparser
  - pip install selenium
  
* Prerequisite program code :  mouse_operations.py
   - file contains all type of operations which human will do on web pages, so whenever its required we can specific operation/action based on requirement in our main program.
   - actions/operations/user_functions are listed below -->
     1. MoveToElement :- which moves the control to specific xpath 
     2. GetAttribute  :- which returns the attribute(either href,text,html link,name) based on input string value to the function
     3. LoadPage :- which waits the webpage to load a specific content/xpath to be present on the loaded webpage content.
     4. MouseClick :- which performs click operation on the specific element/xpath.
     5. Clear :- which performs clear operation on the specifc element.
     6. MouseClickAndSendKeys :- which performs click,clear operations then it will sends the given value on function to the element.
     7. MouseClickandSendKeysEnter :- which does the operation of MouseClickAndSendKeys, then hits the enter key.
     8. Dropdown_Options :- which will returns the all listed options on the particular xpath/element.
     9. scroll_down :- which scrolls down the webpage content by a mentioned offset value .
     
* Prerequisite property file : OnlineDataEntry.properties
  - file contains useful & input commands to the main program code , which contains the xpath address on it and also user can change the requirement based on his/her interest.
  
* Main program code : OnlineDataEntry.py
  - This is the our main program file , which divides the whole actions into subparts as listed below :
      1. Opening website & with provided login info from properties file 
      2. Adding the few option settings to Chrome browser .
      3. Opening web browser with 'form filling work' data from 'OnlineDataEntry.properties' file on onlinedataentry job portal. 
      4. First program will read the contents of table & also keep on adding the data/contens on to the field.


## webautomation_with_unittest.py

  This Program will imports the unittest module & runs the programs unit by unit based on the requirement.
