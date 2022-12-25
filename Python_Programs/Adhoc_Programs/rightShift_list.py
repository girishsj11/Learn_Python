#Write a Python program that rotates an array by n positions to the right.

#input - l=[1,2,3,4,5,6] by 2 positions to the right
#output -  l=[5,6,1,2,3,4]

def right_shift(l,n):
    print("Before right shift of {} time the list is {}".format(n,l))
    for i in range(n):
        l.insert(i,l[-n+i])
        l.pop(-n+i)
    print("After right shift of {} time the list is {}".format(n,l))
    
if __name__ == "__main__":
    l=list(map(lambda x:int(x) , input().split()))
    n=input("Enter the number of times right shift is needed on the list")
    right_shift(l,n)
