# factorial.py

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 12:22:02 2020
@author: gshambul
"""

## Method 1
number = int(input("Enter the number , for which you wanted the program to print its factorial answer : "))



#function to calculate the factorial given user input integer number 
def factorial(number):
    factorial = 1 #initial value for the answer is 1 , as we know 0! & 1! is 1
    #and also anything multiply with 1 is anything .
    if(number<=1):
        return factorial
    else:
        factorial = number * factorial(number-1)
    return factorial


if __name__ == "__main__":
    factorial_answer = factorial(number)
    print("The given number is : {} and its equivalent factorial answer is : {}".format(number,factorial_answer))
    

    
    
    
    
    
## Method 2

def factorial(num):
    '''   
    0! = 1
    1! = 1
    2! = 2
    3! = 3*2*1 = 6
    4! = 4*3*2*1 = 24
    5! = 5*4! = 120
    '''
    
    if(num<0):
        return ("please enter +ve value")
    else:
        flag = 1
        while(num>=0):
            if(num==0):
                return flag
            else:
                flag = flag * num
                num = num-1
        return flag

if __name__ == "__main__":
    num = int(input("Enter a number to get its factorial : "))    
    print(factorial(num))


    
    
    
    
    
    

## Method 3

if __name__ == "__main__":
    fact = 1
    num = int(input("Enter a number to get its factorial : ")) 
    if(num<0):
        print("please enter +ve value")
    else:    
        for i in range(1,num+1):
            fact *= i
        print(fact)
