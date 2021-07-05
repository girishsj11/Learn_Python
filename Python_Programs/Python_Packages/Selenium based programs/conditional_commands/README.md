### conditional_command Actions onto Web page by using selenium+python

1. load the packages

   - selenium.webdriver
   - from selenium.webdriver.chrome.options if needed
   - from time import sleep module
  
2. create instance suitable driver & also provide its executable path as one of parameter to it, which you have it in your system

   - Chrome : webdriver.Chrome(executable_path="./chromedriver")
   - Internet explorer : webdriver.Ie()
   - Firefox : webdriver.Firefox() 
  
3. Create the options which is suitable for user to watch .
 
4. Load the url page link to the driver with predefined options which are predefined above.

5. once webpage is loaded , it will look for the elements which user entered in main program.

   - first_name_field
   - gender_field
   
6. After that based on web page element status , the program will displays either True or False.

   - element.is_enabled():
    
    	The is enabled action verifies if an element is enabled on the web page and can be executed on all web elements. & is_enabled method returns a boolean value specifying whether the target element is enabled or not displayed on the web page.
    	
   - element.is_displayed():
   
    	The is displayed action verifies if an element is displayed on the web page and can be executed on all web elements. & is_displayed method returns a boolean value specifying whether the target element is displayed or not displayed on the web page.


   - element.is_selected():
    
    	The is_selected action verifies if an element is selected right now on the web page and can be executed only on a radio button, options in select, and checkbox  WebElements, When executed on other elements, it will return false.
