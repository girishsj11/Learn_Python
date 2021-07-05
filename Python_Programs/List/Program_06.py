# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 10:27:11 2020
@author: gshambul
"""

'''
Program will display the number of occurance count of each unique values which is present in list .
'''


def list_creation(user_list):
    element_count = int(input("Enter the number of elements to be present in user list : "))
    if(element_count>0):
        for _ in range(1,element_count+1):
            print("Enter {} element : ".format(_))
            user_list.append(int(input()))
    else:
        print("Please provide the element_count value greater than zero ")
        exit(0)


#method - 2 to create list
'''
def list_creation(user_list):
    print("Enter the list elements with space between each others : \n")
    user_list = list(map(lambda x:int(x), input().split()))
    return user_list

'''
        
  
    
if __name__ == "__main__" :
    user_list = list()
    list_creation(user_list)
    print("user input list is : ",user_list)
    print("Element --> Occurence count")
    for i in set(user_list):
        print(i," --> ",user_list.count(i))
