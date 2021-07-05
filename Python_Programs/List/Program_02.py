# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 22:28:42 2020
@author: giri
"""

'''
Convert two lists into a dictionary
'''

keys = ['Ten', 'Twenty', 'Thirty','Fourtee']
values = [10, 20, 30, 40]

dictionary = {key:value for key,value in zip(keys,values)} 
# another method of creating it :- 
#dictionary = dict(zip(keys,values))
print(dictionary)
