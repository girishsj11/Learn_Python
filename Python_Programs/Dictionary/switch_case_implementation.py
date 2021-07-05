# switch_case_implementation.py

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 17:28:21 2020
@author: giri
"""
def Switch_case_implementation(operator,num1,num2):
    '''
        using dictionary , we can declare 'n' number of operation or condition 
        & we can use it as like a swicth case statement which C language & other language supports.
        
    Parameters
    ----------
    operator : TYPE -> String
        DESCRIPTION -> with help of operator the function will returns its operation. 
    num1 : TYPE -> int
        DESCRIPTION -> a integer number to do all mathematical operations
    num2 : TYPE -> int
        DESCRIPTION -> a integer number to do all mathematical operations
    Returns
    -------
            the function returns the expresions/operations from 2 input numbers with help of operator variable.
            
    '''
    switch_case = {
                   'add' : (lambda : num1+num2),
                   'mul' : (lambda : num1*num2),
                   'sub' : (lambda : num1-num2),
                   'div' : (lambda : num1/num2),
                   'floor_div' : (lambda : num1//num2),
                   'rem' : (lambda : num1%num2),
                   'pow' : (lambda : num1**num2)
                    }
    return (switch_case.get(operator,(lambda : None))())


if __name__ == "__main__":
    num1 = int(input("Enter the first integer number : "))
    num2 = int(input("Enter the second integer number : "))
    print(Switch_case_implementation('add', num1, num2))
    print(Switch_case_implementation('mul', num1, num2))
    print(Switch_case_implementation('sub', num1, num2))
    print(Switch_case_implementation('div', num1, num2))
    print(Switch_case_implementation('floor_div', num1, num2))
    print(Switch_case_implementation('rem', num1, num2))
    print(Switch_case_implementation('pow', num1, num2))
    print(Switch_case_implementation('+', num1, num2))
    '''
    Where the last statement has a symbol/operator ,
    which doesnot exists in dictionary which user declared , 
    so it will display the default value as None
    
    '''
