'''

Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.

'''

in_list = [-10,-10,10]
result = 1
if(len(in_list)>=3):
    for i in range(0,3):
        result = result * abs(in_list[i])
        
    print("Result is : ",result)

else:
    print("Due to less number of elements in list , you can't process further !! ")
