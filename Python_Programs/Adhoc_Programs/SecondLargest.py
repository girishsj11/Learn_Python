#Finding out the second largest number in a list

#way-1
l=[1,2,3,5,9,10,0,8,10,9,1,4]
l=list(set(l))
l.sort()
print(l[-2])

#way-2
l=[1,2,3,5,9,10,0,8,10,9,1,4]
l=list(set(l))
l.remove(max(l))
print(max(l))

#way-3
l=[1,2,3,5,9,10,0,8,10,9,1,4]
l=list(set(l))
l.reverse() or l.sort(reverse=True)
print(l[1])





