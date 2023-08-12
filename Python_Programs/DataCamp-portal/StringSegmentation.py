#StringSegmentation.py

'''
list_of_words = ["data", "camp", "cam", "lack"]
string = "datacamp"
'''



def segmentation(words,s):
    for i in range(1,len(s)+1):
        first_str = s[0:i]
        if first_str in words:
            second_str = s[i:]
            if(second_str in words or segmentation(words,second_str)):
                return True
    return False
    



if __name__ == "__main__":
    words = ['data','cam','camp','fung']
    string = 'datafang'
    print(segmentation(words,string))
