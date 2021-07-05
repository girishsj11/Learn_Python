# largestNumber.py

'''
For n = 2, the output should be
largestNumber(n) = 99.
Input/Output
[execution time limit] 4 seconds (py3)
[input] integer n
Guaranteed constraints:
1 ≤ n ≤ 9.
[output] integer
The largest integer of length n.
'''

def largestNumber(n):
    reference = '9'
    if(n==1):
        return int(reference)
    elif(n>1 and n<=10):
        return int(reference*n)
    else:
        return ("Exceeded/below the range value")

if __name__ == "__main__":
    n =  int(input("Enter the number to get its largest number of digits : "))
    print(largestNumber(n))
