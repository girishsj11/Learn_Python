#converting the nested list to flat list
'''
Ex- 
l = [0, [1,2,3], [4,5,[6,7,8,[9,10,11]], [12, 13]], 15, 16]
# result should be flatten
# [0, 1, 2, 3, 4, 5, 6, ----------- 16]
'''

def NestListtoFlatList(l_in):
    for i in l_in:
        if type(i) is list:
            NestListtoFlatList(i)
        else:
            l_out.append(i)

if __name__=="__main__":
    l_in = [0, [1,2,3], [4,5,[6,7,8,[9,10,11]], [12, 13]], 15, 16] #Enter your list of elements
    l_out = list()
    NestListtoFlatList(l_in)
    print(l_in,"\n",l_out)
            
