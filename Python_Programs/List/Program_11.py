'''
Program_11

separating the zero's from list to end of the array & sorting the other numbers
(*rather than 0) in a order.

Ex : 
    input = [1,5,0,3,0,0,2,4]
    output : [1,2,3,4,5,0,0,0]

'''
def function():
    print("Enter the list elements space between each other : ")
    l = list(map(lambda x:int(x) , input().split()))
    print("Before function call :",l)
    count = l.count(0)
    l.sort()
    while(count>0):
        l.remove(l[0])
        count -= 1
        l.append(0)
        
    print("After function call :",l)


if __name__ == "__main__":
    function()
