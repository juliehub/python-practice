#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0

    # initiate a temporary array to store the initial position of input arr
    temp = [0] * (len(arr) + 1)
    
    # arr = [4, 3, 1, 2] --> temp = [0, 2, 3, 1, 0]
    for pos, val in enumerate(arr):
        temp[val] = pos
        pos += 1
    
    # iterate through the original array
    # arr = [4, 3, 1, 2] --> temp = [0, 2, 3, 1, 0]
    # swap 4 and 1: arr = [1, 3, 4, 2] --> temp = [0, 2, 3, 1, 2]
    # swap 2 and 3: arr = [1, 2, 4, 3] --> temp = [0, 2, 3, 3, 2]
    # swap 4 and 3: arr = [1, 2, 3, 4] --> temp = [0, 2, 3, 3, 3]
    for i in range(len(arr)):
        # swap only if value at i is not at the position i+1
        if arr[i] != i+1:
            swaps += 1
            # hold value arr[i] in t variable for swapping
            # iteration 1: swap 4 and 1
            # arr = [1, 3, 4, 2] and temp = [0, 2, 3, 1, 2]
            t = arr[i]
            arr[i] = i+1
            # original position of 1 is temp[i+1] (temp[1])=2)
            arr[temp[i+1]] = t
            # update temp position of the current number being swapped to temp[1]=2
            temp[t] = temp[i+1]
    return swaps

if __name__ == '__main__':

    os.environ['OUTPUT_PATH'] = 'output.txt'

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input("Enter the size of array:"))

    arr = list(map(int, input("Enter an array:").rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
