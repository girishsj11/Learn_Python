'''
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.
'''

def Bubble_sort(list1):
    length = len(list1)
    print("Before sorting : ",list1)
    for i in range(length-1):
        for j in range(length-i-1):
            if(list1[j]>list1[j+1]):
                list1[j],list1[j+1] = list1[j+1],list1[j]
    print("After sorting : ",list1)
    
    
    
if __name__ == "__main__":
    print("Enter the list elements with a space in between each elements")
    list1 = list(map(labmda x:int(x) , input().split()))
    Bubble_sort(list1)
