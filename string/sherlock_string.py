#!/bin/python3
"""
Sherlock considers a string to be valid if all
characters of the string appear the same number
of times. It is also valid if he can remove just
character at  index in the string, and the remaining
characters will occur the same number of times. Given 
a string , determine if it is valid. If so, return YES
, otherwise return NO.
"""
from collections import Counter
import math
import os
import random
import re
import sys

def isValid(s):
    """
    Given a string , determine if it is valid. 
    If so, return YES, otherwise return NO.
    """
    c = Counter(s)
    freq = Counter(c.values())
    # return "YES" if all characters appear with the same frequency
    # example: abc, aabbcc, aaabbbccc
    if len(freq) == 1:
        return "YES"
    # example: aaabbbcc, aaabbcc
    # we can only remove 1 character, so we only consider frequency group with 2 frequencies
    elif len(freq) == 2:
        key_max = max(freq.keys())
        key_min = min(freq.keys())
        # we can only remove 1 character, so freq[key_max] or freq[key_min] must be 1
        # remove 1 character in a group
        # example: aaabb, aaaabbb,aaabbbb
        if key_max - key_min == 1 and freq[key_max] == 1:
            return "YES"
        # remove the odd character out, it only appears once
        # example: aabbc, aaaabbbbc
        elif key_min == 1 and freq[key_min] == 1:
            return "YES"
    # example: aaabbbcc, aaabbc
    return "NO"

if __name__ == '__main__':
    #fptr = sys.stdout
    os.environ['OUTPUT_PATH'] = 'output.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input("Enter your string here:")

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
