def counting(A, m):
    """
    This function returns an array/dictionary of counters.
    Each number may be counted in the array by using an index that corresponds to the value of the given number.
    
    Args:
    A: list of n itegers
    (1 <=m <=1,000,000)
    
    O(n + m)
    """
    n = len(A)
    count = [0] * (m + 1)
    
    for k in range(n):
        count[A[k]] += 1
    
    return count
    
def fast_swap(A, B, m):
    """
    This function checks whether there is a swap operation which can be performed on these
    arrays in such a way that the sum of elements in array A equals the sum of elements in
    array B after the swap. By swap operation we mean picking one element from array A and
    one element from array B and exchanging them.

    Args:
    A: list of n itegers
    B: list of n itegers
    (1 <=m <=1,000,000)
    
    O(n + m)
    """
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)
    print("Array A:",A)
    print("Array B:",B)
    print("sum_a:",sum_a)
    print("sum_b:",sum_b)
      
    d = sum_b - sum_a
    print("Sum difference:",d)
    
    # For every element of array B, we assume that we will swap it with some element from
    # array A. The difference d tells us the value from array A that we are interested in swapping,
    # because only one value will cause the two totals to be equal. The occurrence of this value can
    # be found in constant time from the array used for counting.
    
    if d % 2 == 1:
        print("Sum difference is odd. No solution to swap.")
        return False
    
    print("Sum difference is even. Maybe there is a solution to swap.")
    
    # We are interested in in swapping B[i]-d/2 and A[i]+d/2
    d //= 2
    count = counting(A, m)
    print("Dictionary for A:",count)
    
    for i in range(n):
        # count[B[i]-d] > 0 means there exists an element in A so that we can swap

        if 0 <= B[i] - d and B[i] - d <= m and count[B[i] - d] > 0:
            print("\nFound the 2 numbers to swap at B[i]:",i)
            print("A[i]:",A[i])
            print("B[i]:",B[i])
            print("\nThere is a solution to swap, because...")
            print("B[i] - d:",B[i] - d)
            print("m:",m)
            print("count[B[i] - d]:",count[B[i] - d])
            return True
    return False

#A=[2,3,5,8,10,12]
#B=[1,4,6,7,9,11]
A=[2,4]
B=[1,3]

fast_swap(A,B,12)
