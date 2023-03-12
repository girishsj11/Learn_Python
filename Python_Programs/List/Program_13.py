'''
program to remove multiple repeated item from list without using any looping concepts.
'''
#Need to remove 2 from below list without using looping concepts

l=[1,2,3,4,5,0,55,66,2,3,5,2,1]
print('Before sort',l)
l.sort()
print('After sort',l)
beginning_index = l.index(2)
ending_index = beginning_index+l.count(2)
del l[beginning_index:ending_index]
print('Final list',l)
