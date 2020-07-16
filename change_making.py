def get_num_ways(N,Coins):

    """
    This fuction will return the number of ways to make the amount with those denominations.
    https://www.youtube.com/watch?v=jgiZlGzXMBw
    https://www.geeksforgeeks.org/understanding-the-coin-change-problem-with-dynamic-programming/
    
    Args:
    N: an amount of money
    Coins: a list of coin denominations
    
    Returns:
    the number of ways to make the amount of money with coins of the available denominations.
    
    Example: for amount=44 (44¢) and denominations=[1,2,3] (1¢, 2¢ and 3¢),
    your program would output 4—the number of ways to make 44¢ with those denominations:

    1¢, 1¢, 1¢, 1¢
    1¢, 1¢, 2¢
    1¢, 3¢
    2¢, 2¢
    
    To test this function:
    >>> get_num_ways(4,[1,2,3])
    4
    
    """
    
    # create an array to store the number of ways for each amount from 1 to the amount
    # Index of Array of ways:    [0,  1,  2,  3,  4]     
    # Array of  ways:            [0,  1,  2,  3,  4]
    ways = [0] * (N + 1); 

    # if the amount is zero, there is 1 way to make 0 with 0 coins!
    ways[0]=1
    
    # traverse through the coins
    for i in range(len(Coins)):
        
        # compare coin value with the amount, which is also the index of the array ways
        for j in range(len(ways)):
            # update the ways array if the coin value is less than the amount
            if(Coins[i] <= j):
                ways[j] += ways[int((j-Coins[i]))]
                
    # return the number of ways at the Nth position    
    return ways[N]

def main():
        Coins = [1, 2, 3]; 
        print("The Coins Array:",Coins)
        print(get_num_ways(4, Coins))
        #print(get_num_ways(12, [1,5,10]))
        
if __name__ == "__main__":
    main()
