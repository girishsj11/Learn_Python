# Adhoc_Programs

## FizzBuzz

   **Program Description :** 
   - Program has to print 'Fizz' for the multiple of 3's , and should print 'Buzz' for the multiple of 5's
     and if a number which is multiple of both 3&5 then it should print 'FizzBuzz'.
     if not the program has to print number itself .

## Masking_user_password
   **Program motive :-** Mask the user password which user enters on screen
   
   **Pre-requisite things :**
   - pip install getpass
   - pip install stdiomask
   
   **Program Description :**
   - Masking the user password we have 2 methods which can be implemented by using the 2 packages/modules :
     * getpass
       - Where getpass module will not echo's any password which being entered by user.
     * stdiomask
       - Where stdiomask will prompts the user password as asterix or '*'.

## factorial.py

   - Program will ask user to give input integer number to get a its equivalent factorial number .

## integer_to_roman_conversion 

  Program will do the conversion of real integers to equivalent roman numerals:
  - it will ask user to enter the integer number.
  - it will display its equivalent roman numerals.

## max_out_of_integers

  Program will ask the user to enter one integer number & also ask user to enter one more digit number . 
where the second user input digit will be inserting into each start + end position of digits in the first user input number , prints out the max one .

>Example:

     input = 1234 
     given number = 9 
     output= 12349 , 12394, 12934, 19234,91234
     max_output = 91234

## outlook_mail_send_automation

   **Program motive :-** Sending an automatic mail via outlook app in windows platform

   **Pre-requisite things :**
   - outlook application with email id
 
   **Program execution :** 
   - dispatching the outlook application
   - create items based on request 
   - make the receiver id (To item)
   - have the subject line for the mail initiation 
   - Write the body for the mail automation 
   - if needed any attachment you can add it 
   - then final option is to send 


## quick_sorting_algorithm

  Program will do the sorting algorithm on the list with out using an inbuilt 'list.sort()' method.

- it will ask the number of elemnents  to be present in a list 
- it will ask you enter the elements till hits the count of final (*step 1 result)
- program will displays the list before & after sorting algorthim .

## Palindrome_verification

  The program will ask user to enter a integer number/string , and will check the reverse of it is same as original or not.

## Binary_search

  This search algorithm takes advantage of a collection of elements that is already sorted by ignoring half of the elements after just one comparison. 
1. Compare x with the middle element.
2. If x matches with the middle element, we return the mid index.
3. Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element. Then we apply the algorithm again for the right half.
4. Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.
in a simple words : searching a Target value among the sorted list/array.

## Bubble_sort

  Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order.

## prime_numbers_generations

  Program will generates the prime numbers which is in between the start/lower & end/upper bound values.

## anagram_check

  An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. 

> For example: the word anagram itself can be rearranged into nagaram, also the word binary into brainy and 
  the word adobe into abode.

## start_up
   
   A startup program has to run the python script on every restarts of machine based on the first time input counter value.
> We have written start_up.py script which shows few information before it restarts the local machine , and we have to place the start_up.cmd file 
in startup folder(shell:startup on run command).

## Fibonaci.py

   Generating the fibonaci series for n number terms
   
## ArmstrongNumbers.py

   Write a program to print out all Armstrong numbers between 1 and 500. If sum of cubes of each digit of the number is equal to the number itself, then the number is called an Armstrong number.
> For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 )

## Adding two numbers without using arithmatic operator +

   Adding two numbers with using an arithmatic + operator .
