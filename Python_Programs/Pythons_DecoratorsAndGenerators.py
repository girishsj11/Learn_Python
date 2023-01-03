#Decorators

def decorator_fun(div):
    def inner(a,b):
        if a!=0 and b==0:
            print("Please provide non zero value to b")
        elif a==0 and b==0:
            print("if possible provide non zero values to both a & b")
        else:
            return div(a,b)
    return inner
            

@decorator_fun
def div(a,b):
    print("a & b divided to -",a/b)
    
div(15,5) #3.0
div(10,2) #5.0
div(3,2) #1.5
div(0,5) #0.0
div(5,0) #Message
div(0,0) #Message


#Generators 

'''
simple generator function or generators is -
'''

#method -1 
t=(x for x in range(100)) #tuple comphrension
type(t) #generator type


#method -2
def simple_generator():
    yield 1
    yield 2
    yield 3
    
x=simple_generator()
for i in range(4):
    print(next(x))

'''
output - 

1
2
3
Traceback (most recent call last):

  File "<ipython-input-13-8aba4faeb892>", line 8, in <module>
    print(next(x))

StopIteration
'''



