# Masking_user_password.py

#getpass module

import getpass
password = getpass.getpass("Please Enter your password : ")
'''
The below if else statement is written bcz we are in hope that user never enters wrong password 
otherwise we can store only authorized user & his/her credentials in a list or dictionary , so when user enters his/her username & password , 
it will checks through the dict/list then it will proceed if its in there
else it will discard his/her login. 
'''
if(password=='' or password==' '):
    print("Failure")
else:
    print("Succes")




'''
#stdiomask module
import stdiomask
password = stdiomask.getpass(prompt="Please Enter your password : ",mask='*')
#The below if else statement is written bcz we are in hope that user never enters wrong password 
if(password=='' or password==' '):
    print("Failure")
else:
    print("Succes")
    
    
'''
