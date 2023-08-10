# TrailingZerosInFactorial.py

'''
Given an integer n, return the number of trailing zeroes in n factorial n!
To pass this challenge, you have to first calculate n factorial (n!) and then calculate the number of training zeros. 

steps -
Finding factorial 
In the first step, we will use a while loop to iterate over the n factorial and stop when the n is equal to 1. 

Calculating trailing zeros
In the second step, we will calculate the trailing zero, not the total number of zeros. There is a huge difference. 

Ex : 7! = 5040
The seven factorials have a total of two zeros and only one trailing zero, so our solution should return 1. 

* Convert the factorial number to a string.
* Read it back and apply for a loop.
* If the number is 0, add +1 to the result, otherwise break the loop.
* Returns the result.
'''
def fact(num):
    factorial = 1
    if num==0 or num==1 :
        return factorial
    else:
        factorial = fact(num-1)*num
    return factorial
    

if __name__ == "__main__":
    num = int(input("Enter the number to know its factorial & trailing zeros count in it :"))
    trailing_zeros = 0
    factorial=str(fact(num))
    for zeros in factorial[::-1]:
        if(zeros == '0'):
            trailing_zeros += 1
        else:
            break
    print("given num - {} & its factorial is - {} , trailing zeros count is - {}".format(num,factorial,trailing_zeros)) 
    
