#Factorial number generation
'''
0! = 1
1! = 1
2! = 2x1 = 2
3! = 3x2x1 = 6
4! = 4x3x2x1 = 24
5! = 5x4x3x2x1 = 120
'''

#Way - 1 #using for loop

def factorial(n):
    fact = 1
    if n<0:
        print("Enter +ve number")
    else:
        for i in range(1,n+1):
            fact = fact*i
        print("Factorial answer for {} is {}".format(n,fact))

if __name__=="__main__":
    n=int(input("Enter the number to get its factorial answer : "))
    factorial(n)


#Way - 2 # using recursive method

def factorial(n):
    fact = 1
    if(n==0 or n==1):
        return fact
    elif(n<0):
        return "Enter +ve number"
    else:
         fact = n*factorial(n-1)
    return fact

if __name__=="__main__":
    n=int(input("Enter the number to get its factorial answer : "))
    print(factorial(n))

#way -3 #using generator method

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
        yield fact

if __name__=="__main__":
    n=int(input("Enter the number to get its factorial answer : "))
    for i in factorial(n):
        print(i,end=',')
        
    
