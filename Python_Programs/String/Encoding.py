# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 16:55:37 2021

@author: gsjeenax
"""

'''
Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters as a single count and character. 
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
'''

def encoding(source):
    encoded = ''
    counter = 1
    temp = source[0]
    
    for index in range(1,len(source)):
        if(temp == source[index]):
            counter += 1
            
        if(temp != source[index]):
            encoded += str(counter)+source[index-1]
            temp = source[index]
            counter = 1
            

    encoded += str(counter)+source[index-1]
    
    return (encoded)

   
def decoding(encoded):
    decoded = ''
    for char in range(len(encoded)):
        if(encoded[char].isalpha()):
            decoded += (int(encoded[char-1]) * encoded[char])
            
    return (decoded)
            
        


if __name__ == "__main__":
    source = str(input("Enter the sequence of characters to be encoded : "))
    encoded = encoding(source)
    decoded = decoding(encoded)
    print("Checking the decoded string is same as the source string : input - {}, encoded - {}, decoded - {}".format(source,encoded,decoded))
