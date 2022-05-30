# String

## Exchange_characters

    exchanging the first & last characters on given string & prompting other characters as it is.

    Ex : 
     input:
        'python'
     ouput:
        'nythop'



## Encoding

    Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. 

    Ex : 
     input:
        'AAAABBBCCDAA'
     ouput:
        '4A3B2C1D2A'


## longest_vowel

    Calculating the longest vowel substring length in the give input string .

    Ex :
      input :  'abcedeai'
      output :  3

      input :  'abcd'
      output :  1

      input : 'bcdr'
      output : 0


## unique_characters

    Program shows the unique or non-repeatating characters from the input given string, If it doesn't exist, return -1.

    Ex : 
      
      input : 'abcd'
      output : a b c d

      input : 'pythonpython'
      output : -1


## capitalize_or_decapitalize.py
   
    A function should accepts a string as input &  output wants to either capitalize or decapitalize ,
    each letter based on whether its index number (its position within the string) is divisible by 2.
    
## Balanced_string.py

    We can assign a value to each character in a word, based on their position in the alphabet(a=1,b=2,c=3....z=26).
    A balanced word is one where the sum of values on the left hand side of the word equals to sum of right hand side .
    write a function that returns integer "1" if the word is balanced and "0" if its not.
    return "-1" if the word has odd number of letters.
    
    Example-1 :
        str = "zips" --> 1
        "zips" = "zi|ps" = 26+9 | 16+19 = 35|35 = 1
        
    Example-2 :
        str = "bray" --> 0
        "bray" = "br|ay" = 2+18 | 1+25 = 20|26 = 0
  
    Example-3 :
        str = "abc" --> -1
        "abc" --> length of string is odd numbers

