# CodeSignal app Python challenges 

## addTwoDigits.py

For n = 29, the output should be addTwoDigits(n) = 11.

## amendTheSentence.py

You have been given a string s, which is supposed to be a sentence. However, 
someone forgot to put spaces between the different words, and for some reason they capitalized the first letter of every word. 
Return the sentence after making the following amendments:

Put a single space between the words.
Convert the uppercase letters to lowercase.

***Example:***
> For s = "CodesignalIsAwesome", the output should be - amendTheSentence(s) = "codesignal is awesome";

> For s = "Hello", the output should be - amendTheSentence(s) = "hello"

## baseConversion.py

   Implement a function that, given an integer number n and a base x, converts n from base x to base 16.

***Example:***
> For n = "1302" and x = 5, the output should be - baseConversion(n, x) = "ca".

> Here's why: 13025 = 20210 = ca16.


## countBits.py

  Implement a function that, given an integer n, uses a specific method on it and returns the number of bits in its binary representation.
Note: in this task and most of the following tasks you will be given a code snippet with some part of it replaced by the ellipsis (...). 
Only this part is allowed to be changed.

***Example:***
> For n = 50, the output should be - countBits(n) = 6.
50(10) = 110010(2), a number that consists of 6 digits. Thus, the output should be 6.


## firstDuplicate.py

Given an array a that contains only numbers in the range from 1 to a.length, 
find the first duplicate number for which the second occurrence has the minimal index. 
In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.

***Example:***
> For a = [2, 1, 3, 5, 3, 2], the output should be firstDuplicate(a) = 3.

There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than the second occurrence of 2 does, so the answer is 3.

> For a = [2, 2], the output should be firstDuplicate(a) = 2;

> For a = [2, 4, 3, 5, 1], the output should be firstDuplicate(a) = -1.

***Input/Output***

[execution time limit] 4 seconds (py3)

[input] array.integer a

***Guaranteed constraints:***
1 ≤ a.length ≤ 105,
1 ≤ a[i] ≤ a.length.

***[output] integer***

The element in a that occurs in the array more than once and has the minimal index for its second occurrence. If there are no such elements, return -1.

## largestNumber.py

For n = 2, the output should be largestNumber(n) = 99.

## modulus.py

It frustrates you more than you'd like to admit that the modulus operator in Python can be applied to non-integer values. 
When you write code, you expect the result of the modulus operator to always be an integer, but thanks to Python this isn't always the case.

To fix this, you've decided to write your own modulus operator as a function. Your task is to implement a function that, given a number n, returns -1 if this number is not an integer and n % 2 otherwise. It is guaranteed that if the number represents an integer, it will be written without a decimal point.

***Example:***
> For n = 15, the output should be - modulus(n) = 1;

> For n = 23.12, the output should be - modulus(n) = -1.


## simpleSort.py

To understand how efficient the built-in Python sorting function is, you decided to implement your own simple sorting algorithm and compare its speed to the speed of the Python sorting. Write a function that, given an array of integers arr, sorts its elements in ascending order.
Hint: with Python it's possible to swap several elements in a single line. To solve the task, use this knowledge to fill in both of the blanks (...).

***Example:***
> For arr = [2,4,1,5], the output should be - simpleSort(arr) = [1, 2, 4, 5].


## strstr.py

Avoid using built-in functions to solve this challenge. Implement them yourself, since this is what you would be asked to do during a real interview.
Implement a function that takes two strings, s and x, as arguments and finds the first occurrence of the string x in s. 
The function should return an integer indicating the index in s of the first occurrence of x. If there are no occurrences of x in s, return -1.

***Example:***
> For s = "CodefightsIsAwesome" and x = "IA", the output should be - strstr(s, x) = -1;

> For s = "CodefightsIsAwesome" and x = "IsA", the output should be - strstr(s, x) = 10.

***Input/Output***

[execution time limit] 4 seconds (py3)

***[input] string s & string x***

A string containing only uppercase or lowercase English letters.

***Guaranteed constraints:***
1 ≤ s.length ≤ 106.
1 ≤ x.length ≤ 106.

***[output] integer***

An integer indicating the index of the first occurrence of the string x in s, or -1 if s does not contain x.

## Miss_Rosy.py 

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

***Input Format***
The first line of input consists of the actual number of students in the class, N. 
The second line of input consists of the list (N space-separated elements) presented to you by Miss Rosy as recorded by the voice recognition device.

***Constraints***
1<= N <= 100
1<= List_elements <=N

***Output Format***
Print the roll number of students who were absent in class separated by space.

***Example:***

Input
> 7

> 1 2 3 3 4 6 4

Output
> 5 7
