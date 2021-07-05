# addTwoDigits.py

'''
For n = 29, the output should be
addTwoDigits(n) = 11.
Input/Output
[execution time limit] 4 seconds (py3)
[input] integer n
A positive two-digit integer.
Guaranteed constraints:
10 ≤ n ≤ 99.
[output] integer
The sum of the first and second digits of the input number.
'''

def addTwoDigits(n):
    n=str(n)
    final = 0
    for i in n:
        final+=int(i)

    return final
    
if __name__ == "__main__":
    n = int(input("Enter the number to add all digits in it : "))
    print(addTwiDigits(n))
