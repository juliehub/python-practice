def prefix_sums(A):
    """
    This function calculate of sums of eements in given slice (contiguous segments of array).
    Its main idea uses prefix sums which
    are defined as the consecutive totals of the first 0, 1, 2, . . . , n elements of an array.
    
    Args: 
    A: an array represents number of mushrooms growing on the
    consecutive spots along a road.
    
    Returns:
    an array contains the consecutive sums of the first n elements of an array A
    
    To use:
    >> A=[2,3,7,5,1,3,9]
    >> print(prefix_sums(A))
    [0, 2, 5, 12, 17, 18, 21, 30]
    
    Time Complexity: O(n)
    """
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P


def count_total(P, x, y):
    """
    This function calculates suffix sums, which are the totals of the k last values.
    Args:
    P: an array contains the consecutive sums of the first n elements
    x: an integer, whih is number of elements of a prefix-sum array
    y: an integer, whih is number of elements of a prefix-sum array
    
    Returns: 
    an array suffix sums, which are the totals of the k last values
    or the totals of m slices [x..y] such that 0 <= x <= y < n

    """
    return P[y + 1] - P[x]

def mushrooms(A, k, m):
    """
    This function calculates the maximum number of mushrooms that the mushroom
    picker can collect in m moves
    
    Args:
    a non-empty, zero-indexed array A of n (1 <= n <= 100 000) integers
    a0, a1, . . . , an−1 (0 <= ai <= 1 000). This array represents number of mushrooms growing on the
    consecutive spots along a road.
    
    k: position integer k and m (0 <= k).
    A mushroom picker is at spot number k on the road.
    
    m: number of moves (m < n)
    In one move she moves to an adjacent spot.
    She collects all the mushrooms growing on spotsshe visits.
    
    Returns:
    maximum number of mushrooms that the mushroom picker can collect in m moves
    
    To use:
    >> A=[2,3,7,5,1,3,9]
    >> print("Maximum number of mushrooms:",mushrooms(A,4,6))
    Maximum number of mushrooms: 25
    
    """
    # Note that the best strategy is to move in one direction optionally followed
    # by some moves in the opposite direction. In other words, the mushroom picker should not
    # change direction more than once. With this observation we can find the simplest solution.
    # Make the first p = 0, 1, 2, . . . , m moves in one direction, then the next m − p moves in the
    # opposite direction
    
    # If we make p moves in one direction, we can calculate the maximal opposite location
    # of the mushroom picker.
    # The mushroom picker collects all mushrooms between these extremes.
    # We can calculate the total number of collected mushrooms in constant time by using prefix sums.
    # Time Complexity: O(n+m)
    
    n = len(A)
    result = 0
    
    # calculate the prefix sums for the array A
    pref = prefix_sums(A)
    
    # move to the left first, then move to the right
    # check upper bound of p: 
    # 1+k>p and 1+m>=p => p from index 0 to (min(m,k)+1)
    for p in range(min(m, k) + 1):
        left_pos = k - p
        # right_pos=left_pos + (m - p) = k-p+m-p=k+m-2*p
        # right_pos < n-1 and right_pos >=k so that mushroom picker at least moves back to the original position
        # and does not waste the moves.
        right_pos = min(n - 1, max(k, k + m - 2 * p))
        result = max(result, count_total(pref, left_pos, right_pos))
        
    # move to the rigt first, then move to the left
    for p in range(min(m + 1, n - k)):
        right_pos = k + p
        left_pos = max(0, min(k, k - (m - 2 * p)))
        result = max(result, count_total(pref, left_pos, right_pos))
        
    return result

A=[2,3,7,5,1,3,9]
print(prefix_sums(A))
print("Maximum number of mushrooms:",mushrooms(A,4,6))
