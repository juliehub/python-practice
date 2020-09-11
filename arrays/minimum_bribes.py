#!/bin/python3
"""
It's New Year's Day and everyone's in line for the Wonderland rollercoaster
ride! There are a number of people queued up, and each person wears a sticker
indicating their initial position in the queue. Initial positions increment 1
by 1 from  at the front of the line to n at the back.

Any person in the queue can bribe the person directly in front of them to swap
positions. If two people swap positions, they still wear the same sticker
denoting their original places in line. One person can bribe at most two
others. For example, if n=8 and Person 5 bribes Person 4, the queue will look
like this: 1,2,3,5,4,6,7,8.

Fascinated by this chaotic queue, you decide you must know the minimum number
of bribes that took place to get the queue into its current state!
"""
import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    """
    print an integer representing the minimum number of bribes necessary,
    or "Too chaotic" if the line configuration is not possible.
    """
    bribes = 0

    for i in range(len(q)):
        # original position is q[i]-1
        # returns "Too chaotic" if this person has moved more than 2 positions ahead
        if (q[i] - 1 - i) >2:
            print("Too chaotic")
            return
        # count number of people who overtake a person
        # check for people from original position q[i]-1 to the person just
        # in front of the new position i
        # to make sure we don't try index 0, we replace position q[i]-2 with
        # max(q[i]-2,0)
        for j in range(max(q[i]-2,0),i):
            if q[j] > q[i]:
                bribes += 1 
    print(bribes)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
