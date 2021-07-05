# Miss_Rosy.py

'''
Miss Rosy teaches Mathematics in the college FALTU and is noticing for last few lectures that the turn around in class is not equal to the number of attendance. 
The fest is going on in college and the students are not interested in attending classes. 
The friendship is at its peak and students are taking turns for classes and arranging proxy for their friends. 
They have been successful till now and have become confident. Some of them even call themselves pro. 
One fine day, the proxy was called in class as usual but this time Miss Rosy recognized the student with his voice.
When caught, the student disagreed and said that it was a mistake and Miss Rosy has interpreted his voice incorrectly. 
Miss Rosy let it go but thought of an idea to give attendance to the students present in class only.
In the next lecture, Miss Rosy brought a voice recognition device which would save the voice of students as per their roll number and 
when heard again will present the roll number on which it was heard earlier. 
When the attendance process is complete, it will provide a list which would consist of the number of distinct voices. 
The student are unaware about this device and are all set to call their proxies as usual. Miss Rosy starts the attendance process and the device is performing its actions. After the attendance is complete, the device provides a list. 
Miss Rosy presents the list to you and asks for the roll numbers of students who were not present in class. 
Can you provide her with the roll number of absent students in increasing order.
Note: There is at least one student in the class who is absent.
Input Format
The first line of input consists of the actual number of students in the class, N. 
The second line of input consists of the list (N space-separated elements) presented to you by Miss Rosy as recorded by the voice recognition device.
Constraints
1<= N <= 100
1<= List_elements <=N
Output Format
Print the roll number of students who were absent in class separated by space.
Example : 
Input
7
1 2 3 3 4 6 4
Output
5 7
'''


def main(N,List_elements):
    List_elements.sort()
    k = List_elements[0]
    out_elements = list()
    for i in List_elements:
        if(k not in List_elements):
            out_elements.append(k)
        k +=1
    for element in out_elements:
        print(element,end=' ')


if __name__ == "__main__":
    N = int(input())
    List_elements = list(map(lambda x:int(x) , input().split(' ')))
    main(N,List_elements)
