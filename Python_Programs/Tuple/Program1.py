'''
Program to find out the odd & even numbers from the list of numbers or range of numbers.
Way1 : when the number is been anded with 1 (*binary) ,then if the LSB or last bit of element is 1 then it will be odd number, else even number.
Way2 : when the number is been devided by 2 ,then if the gets remainder 1 then it will be odd number, else even number.
'''

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 12:13:36 2021
@author: gsjeenax
"""

import time
def Way1(start,end):
    '''
    Parameters
    ----------
    start : TYPE (integer)
        starting point for the range function
    end : TYPE (integer)
        ending point for the range function.
    description :
        when the number is been anded with 1 (*binary) 
        then if the LSB or last bit of element is 1 then it will be odd number, else even number.
    Returns
    -------
    None.
    '''
    result = tuple(('odd' if(i&1==1) else 'even' for i in range(start,end)))
    print(result)

def Way2(start,end):
    '''
    Parameters
    ----------
    start : TYPE (integer)
        starting point for the range function
    end : TYPE (integer)
        ending point for the range function.
    description :
        when the number is been devided by 2 ,
        then if the gets remainder 1 then it will be odd number, else even number.
    Returns
    -------
    None.
    '''
    result = tuple(('odd' if(i%2==1) else 'even' for i in range(start,end)))
    print(result)
    

if __name__ == "__main__":
    start = int(input("Enter the starting value to create a range of values : "))
    end = int(input("Enter the ending value to create a range of values : "))
    start_t = time.time()
    Way1(start,end)
    end_t = time.time()
    print("Total time taken for Way1 method to find out even & odd numbers from the range of {} to {} is : {} seconds".format(start,end,end_t-start_t))

    
    time.sleep(1)
    start_t = time.time()
    Way2(start,end)
    end_t = time.time()
    print("Total time taken for Way2 method to find out even & odd numbers from the range of {} to {} is : {} seconds".format(start,end,end_t-start_t))
