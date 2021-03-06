# simpleSort.py

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 12:55:02 2021
@author: giri
"""

'''
To understand how efficient the built-in Python sorting function is, you decided to implement your own simple sorting algorithm and compare its speed to the speed of the Python sorting. Write a function that, given an array of integers arr, sorts its elements in ascending order.
Hint: with Python it's possible to swap several elements in a single line. To solve the task, use this knowledge to fill in both of the blanks (...).
Example
For arr = [2, 4, 1, 5], the output should be
simpleSort(arr) = [1, 2, 4, 5].
'''

def simpleSort(arr):

    n = len(arr)

    for i in range(n):
        j = 0
        stop = n - i
        while j < stop - 1:
            if arr[j] > arr[j + 1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            j += 1
    return arr
