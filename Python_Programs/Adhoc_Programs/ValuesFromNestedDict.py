#ValuesFromNestedDict.py
'''
Accessing & printing the values from nested dictionary
Ex - 
data_in = {
    "key1": {"key11": {"key111": {"key1111": 1}}},
    "key2": {"key22": {"key222": 2}},
    "key3": {"key33": 3},
    "key4": 4
}

data_out = [1,2,3,4]
'''

def NestedDict(data_in):
    for key,value in data_in.items():
        if(value!=int):
            NestedDict(value)
        else:
            data_out.append(value)

if __name__=="__main__":
    data_out = list()
    data_in = {
    "key1": {"key11": {"key111": {"key1111": 1}}},
    "key2": {"key22": {"key222": 2}},
    "key3": {"key33": 3},
    "key4": 4
              }
    NestedDict(data_in)
    print("Values from Nested Dict :- ",data_out)
