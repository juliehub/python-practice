def binary_gap(N):
    """
    This function returns the length of its longest binary gap. 
    The function should return 0 if N doesn't contain a binary gap.
    
    Args:
      N: an integer within the range [1..2,147,483,647]

    Returns:
      the length of the number N's longest binary gap or 0 if N doesn't contain a binary gap.
    
    A binary gap within a positive integer N is any maximal sequence of consecutive zeros
    that is surrounded by ones at both ends in the binary representation of N.
    
    For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
    
    - The number 529 has binary representation 1000010001 and contains two binary gaps:
      one of length 4 and one of length 3.
    - The number 20 has binary representation 10100 and contains one binary gap of length 1.
    - The number 15 has binary representation 1111 and has no binary gaps.
    - The number 32 has binary representation 100000 and has no binary gaps.
    
    To test this function:
    
    1) Given N = 1041 the function should return 5, 
    because N has binary representation 10000010001 and so its longest binary gap is of length 5.
    
    >>> binary_gap(1041)
    5
    
    2) Given N = 32 the function should return 0, 
    because N has binary representation '100000' and thus no binary gaps.
    
    >>> binary_gap(32)
    0
    
    """
    
    # get the binary of number N
    num = bin(N)[2:]
    #print(num)
    
    #get a binary textual representation without the 0b-prefix
    #get_bin = lambda n: format(n, 'b')

    gap=0
    new_gap=0
    
    # 1st digit is always 1
    i=0
    j=0
    k=0
    
    for i in range(len(num)):
        # find the subsequent '1'
        if num[i]=='1' and i > 0:
            k=i
            
            # if there is a sequence of consecutive zeros, calculate the new gap
            if (k>j):
                new_gap = max(gap,(k-j-1))
                gap=new_gap
            
            j=k
                            
    return gap
