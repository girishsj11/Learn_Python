# Conversion_of_list_to_dictionary.py

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 19:00:49 2021
@author: giri
"""

#method 1 

list_in = [1,2,3,4,5]
iterator = iter(list_in)        
dict_out = dict(zip(iterator,iterator))



#method 2

list_in = [1,2,3,4,5]
dict_out = dict()
for key,value in enumerate(list_in):
    dict_out[key] = value
print(dict_out)



#method 3 using dictionary builtin function

list_in=[1,2,3,4,5]
print(dict.fromkeys(list_in,'Value'))







### Encoding user input raw message & again decoding the encoded message 

chars = [chr(x) for x in range(97,97+26)]
values = [x for x in range(1,27)] 

dict1 = dict(zip(chars,values))

#print(char,'\n',value,'\n',dict1)

raw_message = str(input("Enter your favourite word here to encode it : "))
#raw_message = 'hello!@123'
encode_message = ''
decode_message = ''

for char in raw_message.lower():
    if(char in dict1):
        encode_message += str(dict1[char]) + ' '
    else:
        encode_message += char

#print( "encode_message : {} , and its raw_message : {}".format(encode_message,raw_message))

for encode_value in encode_message.strip().split():
    try:
        if(int(encode_value) in dict1.values()):
            for key,value in dict1.items():
                if(int(encode_value) == value):
                    decode_message += key
    except :
        decode_message += encode_value
    
        
                   

print("Raw_message : {} \nEncode_message : {} \nDecode message :{}".format(raw_message,encode_message,decode_message))    
