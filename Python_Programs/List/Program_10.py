'''
program to sort out only the positive numbers on the list , leave the negative numbers as it is.
display the list .
'''
def create_list(x):
    x = list(map(int,input().split()))
    return x

if __name__ == "__main__":
    l1,l2 = list(),list()
    l1 = create_list(l1)
    for i in l1:
        if(i<0):
            l2.append(i)
            l1.remove(i)
        
    l1.sort()
    l2.extend(l1)
    print(l2)
