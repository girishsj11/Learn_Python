#patterns implementation
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 12:24:05 2023

@author: giri
"""

'''
*
**
***
****
*****
'''
for i in range(1,6):
    print('*'*i)


'''
    *
   **
  ***
 **** 
*****
'''
start,end=1,6
for i in range(start,end):
    print(' '*(end-i-1)+'*'*i)
    

'''
*****
****
***
**
*
'''
for i in range(5,0,-1):
    print('*'*i)
    
'''
*****
 ****
  ***
   **
    *
'''
start=6
for i in range(end-1,0,-1):
    print(' '*(end-i-1)+'*'*i)
    
    
'''
    *
   ***
  *****
 *******
*********
'''
start,end = 1,6
for i in range(start,end):
    print(' '*(end-i-1)+'*'*i+'*'*(i-1))

    

'''
*********
 *******
  *****
   ***
    *
'''

start,end=1,6
for i in range(start,end-1):
    print(' '*(i)+'*'*(end-i-1)+'*'*(end-i-2))

'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''
start,end=1,6
for i in range(start,end):
    print(' '*(end-i-1)+'*'*i+'*'*(i-1))

for i in range(start,end-1):
    print(' '*(i)+'*'*(end-i-1)+'*'*(end-i-2))
