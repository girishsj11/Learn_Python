# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 19:59:05 2020
@author: giri
"""

def main(number):
    bin_num = bin(number).split('b')[1]
    print("The equivalent binary code for {} input number is : {}".format(number,bin_num))


if __name__ == "__main__":
    number = int(input("Enter your favourite number : "))
    main(number)
