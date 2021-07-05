# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 22:03:12 2020
@author: giri
"""

'''
Given a two list of numbers create a new list such that 
new list should contain only odd numbers from the first list 
and even numbers from the second list
'''

first_list = [10,33,22,11,0,5,9,10]
second_list = [22,33,44,88,15,3,100]

output_list = list()

for i in first_list:
    if(i%2==1):
        output_list.append(i)
    continue

for i in second_list:
    if(i%2==0):
        output_list.append(i)
    continue


print("First List is :- ",first_list)
print("Second List is :- ",second_list)
print("Output List is :- ",output_list)
