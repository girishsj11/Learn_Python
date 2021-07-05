# daily_coding_2.py

'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6]
'''
print("Enter the list elements with space : ")
input_list  = list(map(int, input().split()))
output_list=list()
temp=1
for i in input_list:
    temp*=i
print("multiplication of all the elements in a given list is:\n",temp)
for i in input_list:
    output_list.append(temp//i)
    
print("input given user list is:\n",input_list)
print("output list is:\n",output_list)
