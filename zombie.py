"""
Algorithm (BFS):
1. Collect all positions of the zombies into a queue. Then we will use this queue for collecting positions of humans only.
2. Find adjacent humans around each enqueued position.
3. Convert them into zombies.
4. Add their positions into a turned-into-zombie queue.
5. Increase number of the hours.
6. Repeat from 2 until all humans on the matrix will be found and processed.
"""

def minHour(rows, columns, grid):
    """
    This function calculates the minimum hours to infect all humans.
    
    Args:
    rows: number of rows of the grid
    columns: number of columns of the grid
    grid: a 2D grid, each cell is either a zombie 1 or a human 0
    
    Returns:
    minimum hours to infect all humans
    
    To use:
    grid=[[0, 1, 1, 0, 1],
         [0, 1, 0, 1, 0],
         [0, 0, 0, 0, 1],
         [0, 1, 0, 0, 0]]
     
    minHour(4,5,grid)
    
    Output: 2

    Explanation:
    At the end of the 1st hour, the status of the grid:
    [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [0, 1, 0, 1, 1],
     [1, 1, 1, 0, 1]]

    At the end of the 2nd hour, the status of the grid:
    [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1]]
    
    """
    # return 0 hour as there is no zombie
    if not rows or not columns:
        return 0
    
    # Create a queue and collect all positions of the zombies into a queue   
    q = [[i,j] for i in range(rows) for j in range(columns) if grid[i][j]==1]
    print("Original q:",q)
    
    # zombies can move to down, up, right, left
    directions = [[1,0],[-1,0],[0,1],[0,-1]]
    time = 0
        
    while True:           
        new = []
        # Turn human into zombies every hour
        for [i,j] in q:
            for d in directions:
                ni = i + d[0]
                nj = j + d[1]
                # Find adjacent humans around each enqueued position
                if 0 <= ni < rows and 0 <= nj < columns and grid[ni][nj] == 0:
                    # Convert them into zombies
                    grid[ni][nj] = 1
                    # Add their positions into a new queue of zombies
                    new.append([ni,nj])
        
        print("\nAt the end of the ",time+1," hour, the status of the grid:")
        print(grid)
                        
        q = new
        print("q:",q)
               
        # Repeat until all humans on the matrix will be found and processed
        # Empty queue, already turn all humans into zombies
        if not q:
            break
            
        #Increase number of the hours
        time += 1
            
    return time

grid=[[0, 1, 1, 0, 1],
     [0, 1, 0, 1, 0],
     [0, 0, 0, 0, 1],
     [0, 1, 0, 0, 0]]

print("\nMinimum hours to infect all humans:",minHour(4,5,grid))
