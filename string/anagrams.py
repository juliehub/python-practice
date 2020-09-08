"""
Given two strings, a and b, that may or may not be of the same length, 
determine the minimum number of character deletions required to make
a and b anagrams. Any characters can be deleted from either of the strings.
"""
from collections import Counter
import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    ct_a = Counter(a)
    ct_b = Counter(b)
    ct_a.subtract(ct_b)
    return sum(abs(i) for i in ct_a.values())

if __name__ == '__main__':
    a="cde"
    b="abc"
    res = makeAnagram(a, b)
    print(res)

