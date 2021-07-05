# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 10:21:47 2021

@author: girishsj11
"""
'''
A function should accepts a string as input &  output wants to either capitalize or decapitalize ,
each letter based on whether its index number (its position within the string) is divisible by 2.
'''


def Way1(a):
    empty=[]
    for i in range(len(a)): 
        if i%2==0:
            empty.append(a[i].upper())
        else:
            empty.append(a[i].lower())

    return ''.join(empty)

print(Way1('hello world'))


def Way2(a):
    empty = [ a[i].upper() if(i%2==0) else a[i].lower() for i in range(len(a))]
    return ''.join(empty)

print(Way1('hello world'))


def Way3(a):
    return (''.join(c.upper() if(i%2==0) else c.lower() for i,c in enumerate(a)))

print(Way1('hello world'))
