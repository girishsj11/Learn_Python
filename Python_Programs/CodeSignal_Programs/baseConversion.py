# baseConversion.py 

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 12:55:02 2021
@author: giri
"""

'''
Your university professor decided to have a little fun and asked the class to implement a function that, given a number n and a base x, converts the number from base x to base 16. To make things more interesting, he announced that the first student to write the solution will have to answer fewer question than the rest of the class during the final exam.
Laughing devilishly, you asked if it was okay to use a language of your choice, and the unsuspecting professor answered "yes". It's settled then: Python is your language of choice!
Now you're bound to win. Implement a function that, given an integer number n and a base x, converts n from base x to base 16.

Example
For n = "1302" and x = 5, the output should be
baseConversion(n, x) = "ca".
Here's why:
13025 = 20210 = ca16.

'''

def baseConversion(n, x):
    return (hex(int(n,x)).split('x'))[1]
