'''
Python Lambda Functions are anonymous function means that the function is without a name. 
As we already know that the def keyword is used to define a normal function in Python. 
imilarly, the lambda keyword is used to define an anonymous function in Python

1. lambda

syntax - lambda agruments:expression
Explanation - A lambda function is a small anonymous function and lambda can take 'n' numbers of arguments , but only one expression .

2. map 

syntax - map(function,iterable)
Explanation - map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.).

3. filter 

syntax - filter(function,iterables)
Explanation - The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.


4. reduce

syntax - 
from functools import reduce 
reduce(function,iterable)

Explanation - The reduce() function in python performs functional computation by taking a function and an iterable (e.g., list, tuple, dictionary, etc.) 
as arguments, and the result is returned after computation (the process of applying the function on the iterable).
The reduce() function in python is defined in the functools module and doesn't return multiple values or any iterator, it just returns a single value as output which is the result of the whole iterable getting reduced to only a single integer or string or boolean.
'''

#input iterable
l=list(range(1,11))

#lmabda
lambda_list = lambda x:x%2
for i in l:
    print(lambda_list(i),end=',')  #1,0,1,0,1,0,1,0,1,0,
    
lambda_list = lambda x:x%2==0
for i in l:
    print(lambda_list(i),end=',')  #True,False,True,False,True,False.....False,
    
#map
map_list = list(map(lambda x:x%2,l))
print(map_list) #1,0,1,0,1,0,1,0,1,0,


map_list = list(map(lambda x:x%2==0,l))
print(map_list) #True,False,True,False,True,False.....False,


#filter 
filter_list = list(filter(lambda x:x%2,l))
print(filter_list)  #[1,3,5,7,9] - odd numbers


filter_list = list(filter(lambda x:x%2==0,l))
print(filter_list)  #[2,4,6,8,10] - even numbers

#reduce
from functools import reduce
reduce_number = reduce(lambda x,y:x+y , l)
print(reduce_number) # 55 which is same as sum(l)



