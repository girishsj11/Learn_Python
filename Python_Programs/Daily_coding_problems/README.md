# ***Daily_coding_problems***

   ### **daily_coding_1.py**
   - Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
   
   ### **daily_coding_2.py**
   - Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6]
   
   ### **daily_coding_4.py**
   - Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, 
find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3

   ### **daily_coding_410.py**
  - You are given an array X of floating-point numbers x1, x2, ... xn. These can be rounded up or down to create a corresponding array Y of integers y1, y2, ... yn.
Write an algorithm that finds an appropriate Y array with the following properties:
      - The rounded sums of both arrays should be equal.
      - The absolute pairwise difference between elements is minimized. In other words, |x1- y1| + |x2- y2| + ... + |xn- yn| should be as small as possible.
        > For example, suppose your input is [1.3, 2.3, 4.4]. In this case you cannot do better than [1, 2, 5], which has an absolute difference of |1.3 - 1| + |2.3 - 2| + |4.4 - 5| = 1.
        
        
   ### **daily_coding_416.py**
  
  - You are in an infinite 2D grid where you can move in any of the 8 directions:
  > (x,y) to
  > (x+1, y),
  > (x - 1, y),
  > (x, y+1), 
  > (x, y-1),
  > (x-1, y-1),
  > (x+1,y+1),
  > (x-1,y+1),
  > (x+1,y-1)

  - You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.
  Example:
  
  *Input:*
 
  > [(0, 0), (1, 1), (1, 2)]
  
  *output:*
  
  > 2
  
  > It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).


   ### **daily_coding_518.py**

   - Given an array of numbers and a number k, determine if there are three entries in the array ,
which add up to the specified number k. For example, given [20, 303, 3, 4, 25] and k = 49, 
return true as 20 + 4 + 25 = 49



   ### **daily_coding_541.py**

   - Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. 
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".


   ### **daily_coding_625.py**
   
   - This problem was asked by Stripe.
Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.
For example, given 156, you should return 3

   ### **daily_coding_626.py**

   - Given a list of integers, return the largest product that can be made by multiplying any three integers.
For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5 , You can assume the list has at least three integers.
