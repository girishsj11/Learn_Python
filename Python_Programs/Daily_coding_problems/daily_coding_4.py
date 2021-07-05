# daily_coding_4.py
'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, 
find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3
'''    

print("Enter the list elements with space : ")
input_list=list(map(int, input().split()))
input_list.sort()
Temp=input_list[0] 
#storing the first index value to start increment on temp value 

for i in range(len(input_list)):
    Temp+=1
    if(Temp not in input_list):
       Target = Temp
       if(Target ==0):
           continue
       break
    continue

if(Target==0):
    Target+=1
    while(Target in input_list):
        Target+=1

print(Target)
