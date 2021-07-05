'''
Program has to print 'Fizz' for the multiple of 3's , and should print 'Buzz' for the multiple of 5's
and if a number which is multiple of both 3&5 then it should print 'FizzBuzz'.
if not the program has to print number itself .
'''

start = int(input("Enter the starting number for the range argument : \t"))
end = int(input("Enter the ending point/number to be in range as a argument : \t "))

def FizzBuzz(start,end):
    if(end>start):

        #way1
        for i in range(start,end+1):
            if(i%3==0 and i%5==0):
                print("FizzBuzz")
            elif(i%3==0):
                print("Fizz")
            elif(i%5==0):
                print("Buzz")
            else:
                print(i)

        '''
        #way2
        for i in range(start,end+1):
            output = ''
            if(i%3==0):
                output='Fizz'
            if(i%5==0):
                output+='Buzz'
            print(output or i)
        
        #way3
        for i in range(start,end+1):
            print(('Fizz'*(i%3<1))+('Buzz'*(i%5<1)) or i)
            
            
        #way4
        [print('FizzBuzz') if(i%3==0 and i%5==0) else print('Fizz') if(i%3==0) else print('Buzz') if(i%5==0) else print(i) for i in range(start,end)]
        '''
    else :
        print("Please provide the end value > start value")


if __name__ == '__main__':
    FizzBuzz(start,end)
