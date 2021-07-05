# Palindrome_verification.py

# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 20:39:51 2020
@author: giri
"""

#Which is similar to palindrome verification

def reverseCheck(number):
    print("original number is : ", number)
    originalNum = number
    reverseNum = 0
    while (number > 0):
        reminder = number % 10
        reverseNum = (reverseNum * 10) + reminder
        number = number // 10
    if (originalNum == reverseNum):
        return True
    else:
        return False




if __name__ == "__main__":
    number = int(input("Enter the integer number to check whether original & its reversal is same or not :"))
    print("The original and reverse number is the same:", reverseCheck(number))


# ------------------------------------------------------------------***************************************------------------------------------------------#
#Which is similar to check the given string has a palindrome in it or not 
import math
def palindrome(string):
    length = math.ceil(len(string)/2)
    count = 0
    for i in range(length):
        if(string[i]==string[-i-1]):
            count+=1
    if(count==length):
        print("Given string is a palindrome")
    else:
        print("Given string is not a palindrome")
    
if __name__ == "__main__":
    string = str(input("Enter the string which you wanted check whether its palindrome in it : "))
    palindrome(string)
