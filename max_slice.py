import sys

def golden_max_slice(A):
    """
    This function returns the maximum sum of a slice in the array.
    
    We are looking for two indices p, q such that the total ap + ap+1 + . . . + aq is maximal.
    We assume that the slice can be empty and its sum equals 0.
    The slice we are looking for may contain negative integers.
    
    Args:
    A: an array of n integers
    
    Returns:
    maximum sum of a slice in the array.
    
    
    Time Complexity: O(n)
    
    To use:
    >> A=[5,-7,3,5,-2,4,-1]
    >> print("maximum sum:", golden_max_slice(A))
    10
    
    """
    # max_slice: the largest sum that ends in that position (final sum we need to retuns)
    # max_ending: "maximum sum of a slice ending in position i" equals max_ending

    INT_MIN=-sys.maxsize -1
    max_ending = max_slice = INT_MIN
    
    for a in A:
        # find a new ending position i+1 only if a is positive
        # the maximum slice ending in position i+1 equals max(a, max_ending+ ai+1)
        max_ending = max(a, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice

    #for i in range(len(A)):
        # find a new ending position i+1 only if a is positive
        # the maximum slice ending in position i+1 equals max(a, max_ending+ ai+1)
        #max_ending = max(A[i], max_ending + A[i])
       # print(max_ending)
       # max_slice = max(max_slice, max_ending)
   #return max_slice


def quadratic_max_slice(A):
    
    INT_MIN=-sys.maxsize -1
    n = len(A)
    result = INT_MIN
    
    for p in range(n):
        sum = 0
        for q in range(p, n):
            sum += A[q]
            result=max(result, sum)
            
    return result

A=[5,-7,3,5,-2,4,-1]
#A=[-5,-7,-3,-1,-2,-4,-5]

print("maximum sum by calling quadratic_max_slice:", quadratic_max_slice(A))
print("maximum sum by calling golden_max_slice:", golden_max_slice(A))
