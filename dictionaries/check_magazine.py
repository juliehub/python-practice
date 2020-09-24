#!/bin/python3
"""
Given the words in the magazine and the words in the ransom note, print Yes if
he can replicate his ransom note exactly using whole words from the magazine;
otherwise, print No.

For example, the note is "Attack at dawn". The magazine contains only
"attack at dawn". The magazine has all the right words, but there's a case
mismatch. The answer is No.
"""
from collections import Counter
import math
import os
import random
import re
import sys

def checkMagazine(magazine, note):
    """
    Print Yes if he can use the magazine to create an untraceable replica of his
    ransom note. Otherwise, print No.
    """
    count_magazine=Counter(magazine)
    count_note=Counter(note)

    diff = count_note - count_magazine

    # not empty counter
    if diff:
        # magazine=['two', 'times', 'three', 'is', 'not', 'four']
        # note=['two', 'times', 'two', 'is', 'four']
        # count_magazine=({'two':1, 'times':1, 'three':1, 'is':1, 'not':1, 'four':1})
        # count_note=({'two':2, 'times':1, 'is':1, 'four':1})
        # diff=({'two':1})
        # diff Counter shows words missing from magazine
        print("No")
    else:
        # magazine=['give', 'me', 'one', 'grand', 'today', 'night']
        # note=['give', 'one', 'grand', 'today']
        # count_magazine=({'give':1, 'me':1, 'one':1, 'grand':1, 'today':1, 'night':1})
        # count_note=({'give':1, 'one':1, 'grand':1, 'today':1})
        # diff=({})
        print("Yes")

if __name__ == '__main__':

    mn = input("Enter numbers of words in the magazine and the note:").split()
    # the numbers of words in the magazine
    m = int(mn[0])
    # the numbers of words in the note
    n = int(mn[1])

    #The third line contains m space-separated strings, each magazine[i].
    magazine = input("Enter words from magazine:").rstrip().split()
    #The third line contains n space-separated strings, each note[i].
    note = input("Enter words in the ransome note:").rstrip().split()

    checkMagazine(magazine, note)
