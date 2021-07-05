### Forward and Backward actions on Web page by using selenium+python

## Navigation_Commands on web browser

1. load the packages

   - selenium.webdriver
   - selenium.webdriver.common.keys 
  
2. create instance suitable driver & also provide its executable path as one of parameter to it, which you have it in your system

   - Chrome : webdriver.Chrome(executable_path="/chromedriver")
   - Internet explorer : webdriver.Ie()
   - Firefox : webdriver.Firefox() 
   
3. Load the url page link to the driver.

4. once webpage is loaded , search/enter some string onto the search bar , let it load

5. click the back button & again click forward button 

   - Just to checking the history of activity which is stored in the session or not.
