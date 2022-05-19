#Program_12.py

'''
Given an array and a value, find if there is a triplet in array whose sum is equal to the given value. 
If there is such a triplet present in array, then print the triplet and return true. Else return false.

Example :-

Input: array = {12, 3, 4, 1, 6, 9}, sum = 24; 
Output: 12, 3, 9 
Explanation: There is a triplet (12, 3 and 9) present 
in the array whose sum is 24. 
Input: array = {1, 2, 3, 4, 5}, sum = 9 
Output: 5, 3, 1 
Explanation: There is a triplet (5, 3 and 1) present 
in the array whose sum is 9.
'''

def main():
  arr = [1,0,2,4,3,5,6]
  target_sum = 6
  count = 0
  print("sum of triple elements equals to target sum : ")
  for i in range(0,len(arr)-2):
    for j in range(i+1,len(arr)-1):
      for k in range(j+1,len(arr)):
        if(target_sum == (arr[i]+arr[j]+arr[k])):
          count+=1
          print(arr[i]+","+arr[j]+","+arr[k])
          
   print("Number of tripletes are equal to the target_sum : ",count)
          
  


if __name__=="__main__":
  main()


