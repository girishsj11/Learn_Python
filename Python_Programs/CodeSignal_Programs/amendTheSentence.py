# amendTheSentence.py 


"""
Created on Tue Jan 26 12:20:46 2021
@author: giri
"""

'''
You have been given a string s, which is supposed to be a sentence. However, someone forgot to put spaces between the different words, and for some reason they capitalized the first letter of every word. Return the sentence after making the following amendments:
Put a single space between the words.
Convert the uppercase letters to lowercase.
Example
For s = "CodesignalIsAwesome", the output should be
amendTheSentence(s) = "codesignal is awesome";
For s = "Hello", the output should be
amendTheSentence(s) = "hello"
'''

def amendTheSentence(s):
    empty = ''
    for char in s:
        if(char.isupper()):
            empty+=' '
            empty+=char.lower()
        else:
            empty+=char
    empty = empty.strip()
    return empty
    
        
    
if __name__ == "__main__":
    print(amendTheSentence("CodesignalIsAwesome"))
    print(amendTheSentence("Hello"))
