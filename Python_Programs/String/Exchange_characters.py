def exhange_char(str):
    print(str[-1]+str[1:len(str)-1]+str[0])

if __name__ == "__main__":
    str = str(input("Enter the string here : "))
    exhange_char(str)

    # or
    # ''.join([str[-1],str[1:len(str)-1],str[0]])
