#!/bin/python3

import math
import os
import random
import re
import sys

def alternatingCharacters(s):
    """
    Find an integer representing the minimum number of deletions to make the alternating string.
    """
    count = 0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
