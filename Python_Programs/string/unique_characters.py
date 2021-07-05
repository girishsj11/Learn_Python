'''
# unique_characters.py

Given a string, find the first non-repeating character in it and return it. 
If it doesn't exist, return -1. # Note: all the input strings are already lowercase.

'''

def solution(S):
    frequency = dict()
    empty = str()

    for char in S.lower():
        if char not in frequency:
            frequency[char] = 1
        else:
            frequency[char] += 1

    keys = list(frequency.keys())

    for key in keys:
        if(frequency[key]==1):
            empty += key+' '

    return (empty or -1)


if __name__ == "__main__":
    print(solution('abcd'))
    print(solution('pythonpython'))
    print(solution('HelloWorld'))
    print(solution('program'))


