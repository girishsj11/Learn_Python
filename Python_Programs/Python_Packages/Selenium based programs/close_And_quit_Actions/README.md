## Close_And_Quit_Actions onto Web page by using selenium+python

### Basic_Commands on web browser

1. load the packages

   - selenium.webdriver
   - from selenium.webdriver.chrome.options
   - from time import sleep module
  
2. create instance suitable driver & also provide its executable path as one of parameter to it, which you have it in your system

   - Chrome : webdriver.Chrome(executable_path="./chromedriver")
   - Internet explorer : webdriver.Ie()
   - Firefox : webdriver.Firefox() 
  
3. Create the options which is suitable for user to watch .
 
4. Load the url page link to the driver with predefined options which are predefined above.

5. once webpage is loaded & it will search for the "click button" , & once its clicked it will opens new tab.

6. finally based on user interest/option the program will close older web window or closes whole web browser & destroys the session.

   - driver.close :
   	     
         only the window that has focus is closed or in a simple words it will closes the parent web window.
   	
   - driver.quit : 
   	
         used to exit the browser, end the session, tabs, pop-ups etc.
