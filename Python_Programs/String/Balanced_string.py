# -*- coding: utf-8 -*-
"""
Created on Mon May 30 11:08:05 2022

@author: gsjeenax
"""
'''
We can assign a value to each character in a word, based on their position
in the alphabet(a=1,b=2,c=3....z=26). A balanced word is one where the sum of values on the left
hand side of the word equals to sum of right hand side .

write a function that returns integer "1" if the word is balanced and "0" if its not.
return "-1" if the word has odd number of letters

Example-1 :
  str = "zips" --> 1
  "zips" = "zi|ps" = 26+9 | 16+19 = 35|35 = 1

Example-2 :
  str = "bray" --> 0
  "bray" = "br|ay" = 2+18 | 1+25 = 20|26 = 0
  
Example-3 :
  str = "abc" --> -1
  "abc" --> length of string is odd numbers
  
'''
def main_action(string):
    chars = [chr(x) for x in range(97,97+26)]
    values = [x for x in range(1,27)]
    dict_chars = dict(zip(chars,values))
    value1 , value2 = 0,0
    
    if(len(string)%2==1):
        return -1
    else:
        for i in range(0,len(string)//2):
            value1 += dict_chars[string[i]] 
        
        for i in range(len(string)//2,len(string)):
            value2 += dict_chars[string[i]]
            
        if(value1==value2):
            return 1
        else:
            return 0
            
        
   
if __name__ == "__main__":
    string = input("please provide the input to check whether its balanced or not ! \n")
    print(main_action(string))
    
    
