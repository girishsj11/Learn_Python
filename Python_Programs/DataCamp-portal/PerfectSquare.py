#PerfectSquare.py

'''
Given a positive integer num, write a function that returns True if num is a perfect square else False.

Steps -
* Finding the square root of the number and converting it into an integer.
* Applying the square to the square root number and checking if it's a perfect square root.
* Returning the result as a boolean. 
'''
if __name__ == "__main__":
    num = int(input("Enter the number to be verified as perfect square or not : "))
    sqr_root = int(num**0.5)
    if(num == (sqr_root**2)):
        print("The given number {} is perfect square number".format(num))
    else:
        print("False")
    
