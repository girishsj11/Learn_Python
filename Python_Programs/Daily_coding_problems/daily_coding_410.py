# daily_coding_410.py
  
'''
This problem was asked by Airbnb.
You are given an array X of floating-point numbers x1, x2, ... xn. These can be rounded up or down to create a corresponding array Y of integers y1, y2, ... yn.
Write an algorithm that finds an appropriate Y array with the following properties:
    The rounded sums of both arrays should be equal.
    The absolute pairwise difference between elements is minimized. In other words, |x1- y1| + |x2- y2| + ... + |xn- yn| should be as small as possible.
For example, suppose your input is [1.3, 2.3, 4.4]. In this case you cannot do better than [1, 2, 5], which has an absolute difference of |1.3 - 1| + |2.3 - 2| + |4.4 - 5| = 1.
'''

import math
if __name__ == "__main__":
    print("Enter the float input list elements with space between each elements : \n ")
    x = list(map(lambda x:float(x), input().split(' ')))
    y = list()
    ansr = 0
    for i in x:
        y.append(math.floor(i))

    for i in range(len(x)):
        ansr += (abs(x[i]-y[i]))
    print("input list created by user : ",x)
    print("second list created based on values from input list : ",y)
    print("Flooring answer to final value : ",math.floor(ansr))
    print("Ceiling answer to final value : ", math.ceil(ansr))
