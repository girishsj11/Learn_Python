# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 16:14:30 2021

@author: gsjeenax
"""


'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.
'''



number = 256
ones_list = []

bin_number = bin(number)
#print(bin_number)
count = 0

for i in bin_number.lstrip('0b'):
    if(i=='1'):
        count+=1
    elif(i=='0'):
        count = 0
    
    ones_list.append(count)
        
print(max(ones_list))
    
    
    

