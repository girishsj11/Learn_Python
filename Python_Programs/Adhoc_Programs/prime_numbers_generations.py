# prime_numbers_generations.py

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 16:00:24 2021
@author: giri
"""

def is_prime(num):
    """Returns True if the number is prime
    else False."""
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True

if __name__ == "__main__":
    lower = int(input("Enter the lower range to generate prime numbers : "))
    upper = int(input("Enter the upper range to generate prime numbers : "))
    list(filter(is_prime,range(lower,upper)))
