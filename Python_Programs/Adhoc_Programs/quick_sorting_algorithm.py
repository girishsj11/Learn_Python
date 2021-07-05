# quick_sorting_algorithm.py

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 18:32:50 2020
@author: Girish_PC
"""


def swap(number1,number2):
    return (number2,number1)
    

def partition(input_list,lower_bound,upper_bound):
    key = input_list[lower_bound]
    start_index = lower_bound
    end_index = upper_bound

    while(start_index < end_index):
        while(input_list[start_index] <= key):
            start_index+=1
        while(input_list[end_index] > key):
            end_index-=1
        if(start_index < end_index):
            input_list[start_index],input_list[end_index] = swap(input_list[start_index],input_list[end_index])
            
    input_list[lower_bound],input_list[end_index] = swap(input_list[lower_bound],input_list[end_index])
    return end_index



def sorting(input_list,lower_bound,upper_bound):
    if(lower_bound<upper_bound):
        locality = partition(input_list,lower_bound,upper_bound)
        sorting(input_list,lower_bound,locality-1)
        sorting(input_list,locality+1,upper_bound)



def menu():
    print("Welcome to sorting algorithm with out using an inbuilt sorting function !!! ")
    element=int(input("Enter the number of elements to be present in a list : "))
    input_list=list()
    print("Enter the elements of input list : \n")
    for i in range(0,element):
        print("Enter the ",i+1, "element onto the input list ---> ",end="")
        input_list.append(int(input()))
        
    print("The input list was before sorting : \n ",input_list)
    #print("before_sorting : ",time.process_time())
    lower_bound = 0
    upper_bound = len(input_list)-1
    sorting(input_list,lower_bound,upper_bound)
    #print("after_sorting : ",time.process_time())
    print("The input list is after sorting : \n ",input_list)
    print()
    

if __name__ == '__main__':
    menu()
    input("Enter any key to exit")
