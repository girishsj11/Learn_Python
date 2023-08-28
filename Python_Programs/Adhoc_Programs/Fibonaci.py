#Fibonaci series generation

#Way-1  #using normal loop/iterative concept & list data type


def fibonaci(n):
    fib=[0,1]
    if(n>2):
        for i in range(2,n):
            fib.append(fib[i-2]+fib[i-1])
        print("series of fibonaci - {} upto range of numbers - {}".format(fib,n))
        print("{}th series of fibonci number is - {}".format(n,fib[-1]))
    else:
        print(fib)

if __name__=="__main__":
    n=int(input("Enter the number to get series/range of fibonaci numbers : "))
    fibonaci(n)


#Way-2 #using while loop but not with list/any data type

def fibonaci(n):
    x,y=0,1
    if(n>0):
        while(n>0):
            print(x,end=' ')
            x,y = y,x+y
            n -= 1
    else:
        print(x,y)
    
    
if __name__=="__main__":
    n=int(input("Enter the number to get series/range of fibonaci numbers : "))
    fibonaci(n)


#Way-3 #using recursive function/method

def fibonaci(n):
    if(n<=1):
        return n
    else:
        return (fibonaci(n-1)+fibonaci(n-2))

if __name__=="__main__":
    n=int(input("Enter the number to get series/range of fibonaci numbers : "))
    if(n<=0):
        print("Enter a number greater than zero ")
    else:
        for i in range(n):
            print(fibonaci(i),end=' ')


#Way-4 #using generator function

def fibonaci():
    x,y=0,1
    while True:
        yield x
        x,y = y,x+y


if __name__ == "__main__":
    n=int(input("Enter the number to get series/range of fibonaci numbers : "))
    if(n<=0):
        print("Enter a number greater than zero ")
    else:
        fib=fibonaci()
        for i in range(n):
            print(next(fib),end=' ')

