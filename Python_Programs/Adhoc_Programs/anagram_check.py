#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 19:14:07 2021
@author: giri
"""

'''
Anagram Program in python
An anagram is a word or phrase formed by rearranging the letters of a 
different word or phrase, typically using all the original letters 
exactly once. 
For example: the word anagram itself can be rearranged 
into nagaram, also the word binary into brainy and 
the word adobe into abode.
'''


def anagram_check():
    S1 = str(input("Enter the first string : "))
    S2 = str(input("Enter the second string : "))
    if(len(S1)==len(S2)):
        equal_chars = []
        for char in S1:
            if(S1.count(char)==S2.count(char)):
                equal_chars.append(1)
            else:
                equal_chars.append(0)
        if(equal_chars.count(0)==0):
            print("Given words are anagram words")
        else:
            print("Not an anagram words")
            
    
    else:
        print("Not an anagram words due to mismatch in length of a word ")

if __name__ == "__main__":
    anagram_check()
