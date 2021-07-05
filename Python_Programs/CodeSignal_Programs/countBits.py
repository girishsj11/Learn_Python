#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 12:55:02 2021
@author: giri
"""
'''
Implement a function that, given an integer n, uses a specific method on it and returns the number of bits in its binary representation.
Note: in this task and most of the following tasks you will be given a code snippet with some part of it replaced by the ellipsis (...). Only this part is allowed to be changed.
Example
For n = 50, the output should be
countBits(n) = 6.
50(10) = 110010(2), a number that consists of 6 digits. T
hus, the output should be 6.
'''

def countBits(n):
    return n.bit_length()
