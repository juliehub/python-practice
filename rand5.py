from collections import defaultdict
import random

def rand5(rand7):
    """
    This function generates a random integer from 1 to 5.
    
    Args:
    rand7: function rand7() that generates a random integer from 1 to 7
    
    Returns:
    A random integer from 1 to 5.
    
    To use:
    rand5()
    """
    return (rand7 % 5 + 1)


def main():
    d = defaultdict(int)

    for i in range(10000):
        num = rand5(random.randint(1,7))
        d[num]+=1
        
    print("Distribution for random number:", d)
        
if __name__ == "__main__":
    main()
