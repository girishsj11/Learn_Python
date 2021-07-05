#longest_vowel.py

def longest_vowel(S):
    count , longest = 0 , 0
    for char in S.lower():
        if(char in ['a','e','i','o','u']):
            count += 1
        else:
            longest = max(count , longest)
            count = 0 #making it zero since when it hits non vowel character
    print("The longest vowel length among the string {} is - {}".format(S,max(count , longest)))


if __name__ == "__main__":
    S = str(input("Enter your string here : \n"))
    longest_vowel(S)
