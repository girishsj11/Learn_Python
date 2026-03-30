"""
This module checks the given two words are anagram or not!
"""
def is_anagram_words(first_word:str,second_word:str)->bool:
    """
    Anagram Program in python
    An anagram is a word or phrase formed by rearranging the letters of a
    different word or phrase, typically using all the original letters
    exactly once.
    For example: the word anagram itself can be rearranged
    into nagaram, also the word binary into brainy and
    the word adobe into abode.
    """
    return sorted(first_word) == sorted(second_word)

if __name__ == "__main__":
    str1 = input("Enter the first string : ")
    str2 = input("Enter the second string : ")
    if len(str1) == len(str2):
        print(f"given strings - {str1} & {str2} were anagram! -"
              f" {is_anagram_words(str1.lower(),str2.lower())}")
    else:
        print(f"Length of each words {len(str1)} != {len(str2)},so they can't be anagram words!")
