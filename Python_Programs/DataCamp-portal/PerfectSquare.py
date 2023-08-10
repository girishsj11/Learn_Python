#PerfectSquare.py

'''
Given a positive integer num, write a function that returns True if num is a perfect square else False.
'''
if __name__ == "__main__":
    num = int(input("Enter the number to be verified as perfect square or not : "))
    sqr_root = int(num**0.5)
    if(num == (sqr_root**2)):
        print("The given number {} is perfect square number".format(num))
    else:
        print("False")
    
