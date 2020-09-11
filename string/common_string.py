#!/bin/python3
"""
https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
Watch the explanation for Dynamic Programming here:
https://www.youtube.com/watch?v=ASoaQq66foQ
A string is said to be a child of a another string if it can be formed by
deleting 0 or more characters from the other string. Given two strings of 
equal length, what's the longest string that can be constructed such that
it is a child of both?
Test Cases:
1. 
HARRY
SALLY
2.
SHINCHAN
NOHARAAA
3.
ABCDEF
FBDAMN
"""
import math
import os
import random
import re
import sys

def commonChild(s1, s2):
    m = len(s1)
    n = len(s2)
    # Create 2 arrays with length n+1 to store the LCS sequence for each step
    # of the calculation
    # Note that there is no common child string if one of the parent string is empty.
    # When an empty sequence is compared with a non-empty sequence,
    # the longest common subsequence is always an empty sequence.
    prev, cur = [0]*(n+1), [0]*(n+1)

    # for each chacrater in the 1st string,
    # compare it to the character of the 2nd string
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                cur[j] = 1 + prev[j-1]
            else:
                if cur[j-1] > prev[j]:
                    cur[j] = cur[j-1]
                else:
                    cur[j] = prev[j]
        # assign the current array for the next iteration
        # temp = prev
        # prev = cur
        # cur = temp
        cur, prev = prev, cur

    # return the last value, which is the length of the longest common string
    return prev[n]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input("Enter your 1st string here:")

    s2 = input("Enter your 2nd string here:")

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
