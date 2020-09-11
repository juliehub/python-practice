#!/bin/python3
"""
John works at a clothing store. He has a large pile of socks that
he must pair by color for sale. Given an array of integers representing
the color of each sock, determine how many pairs of socks with matching
colors there are.

For example, there are n=7 socks with colors ar=[1,2,1,2,1,3,2]. There is
one pair of color 1 and one of color 2. There are three odd socks left,
one of each color. The number of pairs is 2.
Complete the sockMerchant function in the editor below. It must return an
integer representing the number of matching pairs of socks that are available.
"""
from collections import Counter
import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    """
    Returns the total number of matching pairs of socks that John can sell.
    """
    ct_ar = Counter(ar)
    sum = 0
    for i in ct_ar:
            sum = sum + ct_ar[i]//2
    return sum

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'output.txt'

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input("Enter the number of socks:"))

    ar = list(map(int, input("Enter a list of space-separated integers describing the colors:").rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
