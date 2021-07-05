# CodingBat Python challenges

## Warmup - 1 > sleep_in

    Warmup-1 > sleep_in

    The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. 
    We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

        - sleep_in(False, False) → True
        - sleep_in(True, False) → False
        - sleep_in(False, True) → True

## Warmup-1 > monkey_trouble

    We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they 
    are both smiling or if neither of them is smiling. Return True if we are in trouble.


        - monkey_trouble(True, True) → True
        - monkey_trouble(False, False) → True
        - monkey_trouble(True, False) → False

## Warmup-1 > sum_double

    Given two int values, return their sum. Unless the two values are the same, then return double their sum.

        - sum_double(1, 2) → 3
        - sum_double(3, 2) → 5
        - sum_double(2, 2) → 8

## Warmup-1 > diff21

    Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 
    21.


        - diff21(19) → 2
        - diff21(10) → 11
        - diff21(21) → 0

## Warmup-1 > parrot_trouble

    We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the 
    parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.


        - parrot_trouble(True, 6) → True
        - parrot_trouble(True, 7) → False
        - parrot_trouble(False, 6) → False
        - parrot_trouble(False, 21) → False
        - parrot_trouble(False, 23) → False
        - parrot_trouble(True, 23) → True

## Warmup-1 > makes10

    Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

        - makes10(9, 10) → True
        - makes10(9, 9) → False
        - makes10(1, 9) → True

## Warmup-1 > near_hundred

    Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

        - near_hundred(93) → True
        - near_hundred(90) → True
        - near_hundred(89) → False

## Warmup-2 > array123
  
    Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

        - array123([1, 1, 2, 3, 1]) → True
        - array123([1, 1, 2, 4, 1]) → False
        - array123([1, 1, 2, 1, 2, 3]) → True
