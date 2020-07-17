import sys 
    
def max_product(arr):
    """
    This function find the highest product of three numbers from a list
    O(n) Time, O(1) Space
    
    Args:
    arr: a list of integer
    
    Returns:
    the highest product of three numbers from a list
    
    To test this function:
    >> print("Max product", max_product([10,3,5,6,20]))
    Max product 1200
    >> print("Max product", max_product([-10,-3,-5,-6,-20]))
    Max product -90
    >> print("Max product", max_product([1,-4,3,-6,7,0]))
    Max product 168
    
    """
    
    # if size is less than 3, no triplet exists 
    N = len(arr)
    
    if (N < 3):
        return -1
    
    
    # Initialize first maximum, second maximum and third maximum elements
    max1 = -sys.maxsize-1
    max2 = -sys.maxsize-1
    max3 = -sys.maxsize-1

    # Initialize first minimum and second mimimum elements
    min1 = sys.maxsize
    min2 = sys.maxsize
             
    for i in range(N):
        # Scan the array and compute Maximum, second maximum and third maximum element present in the array.
        # min1 min2 max3 max2 max1 arr[i]
        if (arr[i]>max1):
            max3=max2
            max2=max1
            max1=arr[i]
        else:
            # min1 min2 max3 max2 arr[i] max1
            if (arr[i]>max2):
                max3=max2
                max2=arr[i]
            else:
                # min1 min2 max3 arr[i] max2 max1
                if (arr[i]>max3):
                    max3=arr[i]
                
        # Scan the array and compute Minimum and second minimum element present in the array.
        # arr[i] min1 min2 max3 max2 max1
        if (arr[i] < min1):
            min2=min1
            min1=arr[i]
        else:
            # min1 arr[i] min2 max3 max2 max1
            if (arr[i]<min2):
                min2=arr[i]
    
    # Return the maximum of product of Maximum, second maximum and third maximum
    # and product of Minimum, second minimum and Maximum element.
    return max((max1*max2*max3),(min1*min2*max1))

print("Max product", max_product([10,3,5,6,20]))
print("Max product", max_product([-10,-3,-5,-6,-20]))
print("Max product", max_product([1,-4,3,-6,7,0]))
