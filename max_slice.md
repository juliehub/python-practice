Let’s define a problem relating to maximum slices. You are given a sequence of n integers
a0, a1, . . . , an−1 and the task is to find the slice with the largest sum. More precisely, we are
looking for two indices p, q such that the total ap + ap+1 + . . . + aq is maximal. We assume
that the slice can be empty and its sum equals 0.

A=[5,-7,3,5,-2,4,-1]

The slice with the largest sum is made of 4 intergers 3,5,-2,4. The sum of this slice
equals 10 and there is no slice with a larger sum. Notice that the slice we are looking for may
contain negative integers, as shown above.
