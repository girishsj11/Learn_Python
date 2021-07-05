# max_out_of_integers.py

# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 09:39:15 2020
@author: gshambul
"""

'''
input = 1234
given number = 9
output= 12349 , 12394, 12934, 19234,91234
print the max of output list
'''

if __name__ == "__main__":
    input_number=int(input("Enter the input number here : " ))
    user_num=int(input("Enter the number where it will inserting into the start & end of each digit of input_num which is declared eralier : "))
    output_list = list()

    # storing the input number as a list of strings 
    length = str(input_number)
    input_number = str(input_number)
    user_num = str(user_num)

    for i in range(length+1):
        value = int(input_number[:i]+usernum+input_number[i:])
        output_list.append(value)

    print("Values : ")
    for i in output_list:
        print(i)
    
    output_list.sort()
    print("greatest / largest value among is : ",output_list[-1])
