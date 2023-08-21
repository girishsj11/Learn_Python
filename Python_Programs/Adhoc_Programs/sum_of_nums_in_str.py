#sum of the integers from a given string
#i/o:s = "abcaa1anv12hsd234mnxz3and45"
#0/p: result = 1+12+234+3+45

def sum_of_nums_in_str(s):
    numbers,numericals=list(),''
    for char in s:
        if(char.isnumeric()):
            numericals+=char
        else:
            if(len(numericals)>0):
                numbers.append(int(numericals))
                numericals=''
            else:
                pass
    print("integer numbers - {} in a string - {} , and its sum is - {}".format(numbers,s,sum(numbers)))

if __name__=="__main__":
    s=input("Enter the string : ")
    sum_of_nums_in_str(s)
