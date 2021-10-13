'''

This problem was asked by Amazon.

Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

For example, for the input [1, 2, 3, 10], you should return 7.

Do this in O(N) time.

'''

def function(l):
    result = 1 #initial value to be 1
    for i in range(0,len(l)):
        if(l[i]<=result):
            result += l[i]
        else:
            break
    return result

l = [1,1,3,5] #[1,1,1,] [1,2,3,10] [1,2,3,4,5,9]
print(function(l))
