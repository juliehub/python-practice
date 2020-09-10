#!/bin/python3
"""
A string is said to be a special string if either of two conditions is met:

All of the characters are the same, e.g. aaa.
All characters except the middle one are the same, e.g. aadaa.
A special substring is any substring of a string which meets one of those
criteria. Given a string, determine how many special substrings can be formed
from it.
Test cases:
asasd
abcbaba
aaaa
"""
from collections import Counter
import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    # Initialize with n as each character is a special palindromic string
    count = n
    for x in range(n): 
        y = x
        while y < n - 1:
            y += 1
            # if the next charater is the same, found 1 more special substring
            if s[x] == s[y]:
                count += 1
            # if the next character is different, compare the 2 sub-strings
            # before and after this character. Both sub-strings have the same
            # length, which are (y-x-1)
            else:
                if s[x:y] == s[y+1:2*y-x+1]:
                    count += 1
                break

    return count

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'output.txt'

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input("Enter number of characters in the string:"))

    s = input("Enter your string here:")

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
