# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 21:22:53 2020
@author: giri
"""

def is_valid_zip(zip_code):
    """
    Returns whether the input string is a valid (5 digit) zip code
    """
    count = 0
    if (zip_code.isalnum()):
        for i in zip_code:
            if(i.isnumeric()):
                count+=1   
    else:
        return False
    
    if(count==5):
        return True
    else:
        return False
    
      
if __name__ == "__main__":
    zip_code = str(input("Enter your zip code data : "))
    print("The Entered zip code {} data is valid to enter into a system :{}".format(zip_code,is_valid_zip(zip_code)))
