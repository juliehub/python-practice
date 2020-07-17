from collections import defaultdict

def find_unique_num(d_list):
    """
    This function find the unique integer in a list of delivery IDs, which contains many duplicate integers.
    
    Args:
    d_list: a list of IDs, which contains many duplicate integers
    
    Returns:
    a delivery ID, a unique integer
    
    To test this function:
    
    >>> print("Unique integer:", find_unique_num([134, 20, 59, 87, 134, 87, 59]))
    20
    
    """
    u_num = 0
    
    # create a default dictionary that contains the delivery ID as key and value as the count of take off
    # and come back of that particular delivery ID
    d = defaultdict(int)
    
    # iterate through the list for keeping the count
    for i in d_list:
        # The default value is 0 so there is no need to enter the key first
        d[i] += 1
    
    #print(d)
    
    # iterate through the dictionary to find the value of 1
    for i, j in d.items():
        # found the unique number
        if (j==1):
            u_num = i
            # assume there is only 1 missing drone
            return u_num

print("Unique integer:", find_unique_num([134, 20, 59, 87, 134, 87, 59]))
print("Unique integer:", find_unique_num([134, 59, 87, 134, 87, 59]))
