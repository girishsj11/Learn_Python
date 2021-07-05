#Program to make the list with unique elements in it which means removing duplicates from it 

# method 1

'''
We can make it by passing the list into set method , as we are aware of this set is unordered & unique elements data type
'''

def list_creation(in_list):
    print("Please enter the numbers by including space between each elements and enter some duplicate values : \n ")
    in_list = list(map(lambda x:int(x) , input().split(' ')))
    return in_list

if __name__ == "__main__" :
    in_list = list_creation(in_list)
    print("Elements of list with all duplicate values in it : ",in_list)
    print("List with only unique values in it : ",list(set(in_list)))


# method 2

'''
We can make it by removing the duplicate element from the list & finally printing it
'''

'''
def list_creation(in_list):
    print("Please enter the numbers by including space between each elements and enter some duplicate values : \n ")
    in_list = list(map(lambda x:int(x), input().split(' ')))
    return in_list

def remove():
    in_list = list_creation(in_list)
    print("Elements of list with all duplicate values in it : ", in_list)
    for element in in_list:
        if(in_list.count(element)>1):
            in_list.remove(element)
    print("List with only unique values in it : ",in_list)

if __name__ == "__main__" :
    remove()

'''
