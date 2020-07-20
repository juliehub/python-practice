"""
Test cases:
grid = [["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]]
Output: 1

grid = [["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]]
Output: 3

grid = [["1", "1", "0", "0", "0"], 
        ["0", "1", "0", "0", "1"], 
        ["1", "0", "0", "1", "1"], 
        ["0", "0", "0", "0", "0"], 
        ["1", "0", "1", "0", "1"]] 
  
Output: 6
"""
from typing import List

# Recursive 
def getIslandCount(grid,i,j):
    """
    This function sink the current island
    Args:
    grid: a 2d grid map of '1's (land) and '0's (water)
    i: x-axis coordinate
    j: y-axis coordinate
    Returns:
    1 if there is an island
    """
    # check coordinates in bound
    if (i<0) or (i>=len(grid)) or (j<0) or (j>=len(grid[i])) or (grid[i][j]=='0'):
        return 0
        
    #sink the island to mark that we have traversed the coordinates
    grid[i][j]='0'
        
    #find any sibling or so on is also a 1
    getIslandCount(grid,i+1,j)
    getIslandCount(grid,i-1,j)
    getIslandCount(grid,i,j+1)
    getIslandCount(grid,i,j-1)
        
    return 1
            
def numIslands(grid: List[List[str]]) -> int:
    """
    This function returns the number of islands
    Args:
    grid: a 2d grid map of '1's (land) and '0's (water)
    Returns:
    nIsland: thenumber of islands
    """
    if not grid: return 0
    
    nr = len(grid)
    nc = len(grid[0])
        
    nIsland = 0
        
    # loop over every element in the array
    for i in range(nr):
        for j in range(nc):
            # if there is a '1', recursely check any of its siblings and so on is also a 1.
            # we stop when there is no more sibling which is a 1
            if grid[i][j] == '1':
                nIsland += getIslandCount(grid,i,j)   
                
    return nIsland

grid = [["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]]
        
print("Number of islands:",numIslands(grid))
