# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 11:31:33 2021
@author: gsjeenax
"""

'''
daily_coding_518
This problem was asked by Microsoft.
Given an array of numbers and a number k, determine if there are three entries in the array ,
which add up to the specified number k. For example, given [20, 303, 3, 4, 25] and k = 49, 
return true as 20 + 4 + 25 = 49
'''

def main():
    print("Enter the list elements space between each other : ")
    array = list(map(int , input().split(' ')))
    target = int(input("Enter the target value which you wnated to check whether its there \
                       or not by combining 3 elements from the list : "))
    array_size = len(array)
    values = list()
    flag = False
    
    for i in range(0,array_size-2):
        for j in range(i+1,array_size-1):
            for k in range(j+1,array_size):
                if((array[i]+array[j]+array[k])==target):
                    values.extend([array[i],array[j],array[k]])
                    flag = True
                else:
                    continue
            
    if(flag==True):
        print("sum of Elements {} will be equal to target {}".format(values,target))
    else:
        print("None of the 3 elements will be added up together to equal target value !")

if __name__ == "__main__":
    main()
