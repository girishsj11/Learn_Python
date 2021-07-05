# Binary_search.py

'''
This search algorithm takes advantage of a collection of elements that is already sorted by ignoring half of the elements after just one comparison. 
1. Compare x with the middle element.
2. If x matches with the middle element, we return the mid index.
3. Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element. Then we apply the algorithm again for the right half.
4. Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.
in a simple words : searching a Target value among the sorted list/array.
'''

def Binary_search(array,element,start_index,end_index):
    if(start_index>end_index):
        return -1 #if index value is -1 which means element is not there in array list
        
    mid_index = (start_index+end_index)//2
    
    if(element == array[mid_index]):
        return mid_index
        
    else:
        
        if(element<array[mid_index]):
            return Binary_search(array,element,start_index,mid_index-1)
        else:
            return Binary_search(array,element,mid_index+1,end_index)
            

if __name__ == "__main__":
    print("Enter the list elements by having space between each elements : ")
    array = list(map(lambda x:int(x) , input().split()))
    element = int(input("Enter the number which you wanted to search it in array list :"))
    array.sort() #keeping it in a sorted way for the safer side(if user forgots to enter the values in a sorted way)
    print("{} is the index of the element {} is searched in a given array {} ".format(Binary_search(array,element,0,len(array)-1),element,array))
    #if index value is -1 which means element is not there in array list
