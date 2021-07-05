# integer_to_roman_conversion.py

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 15:49:59 2020
@author: gshambul
"""
from datetime import datetime


def main():
    number = int(input("Enter number : "))
    answer = ""
    length = len(integer_numbers)
    temp = number
    if(temp in integer_numbers):
        Roman = integer_numbers.index(temp)
        print("Number : {} , Roman : {}".format(number,roman_letters[Roman]))
    
    else:
        for i in range(length):
            count = int(temp/integer_numbers[i])
            if(count>0):
                answer += count * roman_letters[i]
                temp -= count * integer_numbers[i]
            else:
                continue
        
        print("Input number is : {} & its equivalent roman letters is : {}".format(number,answer))
        

if __name__ == "__main__":
    start = datetime.now()
    roman_letters = ['M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I']
    integer_numbers = [1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1]
    main()
    end = datetime.now()
    print("Total time taken for the program to complete : {} ".format(end-start))
