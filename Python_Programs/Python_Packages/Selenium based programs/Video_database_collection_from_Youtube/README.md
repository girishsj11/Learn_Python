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
