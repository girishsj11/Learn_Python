# daily_coding_416.py

'''
Daily_coding # 416
You are in an infinite 2D grid where you can move in any of the 8 directions:
 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.
Example:
Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
'''

def function(l):
    x = l[0][0]
    y = l[0][1]
    counter = 0
    for i in range(1, len(l)):
        x_next = l[i][0]
        y_next = l[i][1]
        if ((x_next in (x, x + 1, x - 1)) and (y_next in (y, y + 1, y - 1))):
            x = x_next
            y = y_next
            counter += 1
        else:
            counter -= 1
            return ("its against the rules which is declared above !!! ")
    return ("minimum number of steps to achieve to reach end co-ordination from starting point : ", counter)



if __name__ == "__main__":
    list1  = [(0, 0), (1, 1), (1, 3)] #enter your list here
    print(function(list1))
