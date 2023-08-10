#StringSegmentation.py

'''
list_of_words = ["data", "camp", "cam", "lack"]
string = "datacamp"
'''

def segmentation(list_of_words,string):
    segments = []
    for word in list_of_words:
        if word in string:
            segments.append(word)
    print(segments)
    
if __name__ == "__main__":
    string = input("Enter the string to be segmented : ")
    list_of_words = ["data", "camp", "cam", "lack"]
    segmentation(list_of_words,string)
