'''
Write a program to print out all Armstrong numbers between 1 and 500. If sum of cubes of each digit of the number is equal to the number itself, then the number is called an Armstrong number.
For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 )

'''

def ArmstrongNumbers(lower,upper):
    for i in range(lower,upper):
        result = 0
        str_i = str(i)
        for j in str_i:
            result += int(j)**3
        
        if(result==i):
            print("ArmStrong Number : ",i)
        
if __name__=="__main__":
    ArmstrongNumbers(1,500) 
    '''
    output
    Armstrong number :  1
    Armstrong number :  153
    Armstrong number :  370
    Armstrong number :  371
    Armstrong number :  407
    '''

