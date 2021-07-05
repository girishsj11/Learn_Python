# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 20:56:18 2020
@author: giri
"""

'''
competition between user & system generated numbers to conculde who's winner among the random numbers which generates by user , system .
'''

import random

if __name__ == "__main__" :
    print(" user will be having 3 chances to win against system ")
    for _ in range(3):
        user_num = int(input("Enter the your faviourate number between 1-10 : "))
        if(user_num == random.randint(1,10)):
            print("You won the competition !")
        else:
            print("Please try again !!!")
