# Warmup-1:sleep_in.py

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 19:02:11 2021
@author: giri
"""

'''
Warmup-1 > sleep_in
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
'''

# method 1
'''
def sleep_in(weekday, vacation):
  if(weekday==True and vacation==True):
    return True
  if(weekday == True):
    return False
  elif(vacation == True):
    return True
  else:
    return True
'''

# method 2
def sleep_in(weekday, vacation):
  if(weekday==False):
    return True
  else:
    if(vacation==True):
      return True
    else:
      return False

if __name__ == "__main__":
    print(sleep_in(True, False))
    print(sleep_in(True, True))
    print(sleep_in(False, False))
    print(sleep_in(False, True))
