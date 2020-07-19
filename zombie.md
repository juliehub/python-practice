Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour.
Find out how many hours does it take to infect all humans?

**Example:**

Input:

```python
[[0, 1, 1, 0, 1],
 [0, 1, 0, 1, 0],
 [0, 0, 0, 0, 1],
 [0, 1, 0, 0, 0]]
```
Output: 2

Explanation:

At the end of the 1st hour, the status of the grid:
```python
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [0, 1, 0, 1, 1],
 [1, 1, 1, 0, 1]]
```

At the end of the 2nd hour, the status of the grid:
```python
[[1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1]]
 ```
 
 ```python
 int minHours(int rows, int columns, List<List<Integer>> grid) {
	// todo
}
```

Similar problem:
In a 2D array of integer, 2 denotes wall, 1 denotes zombie and 0 denotes human. Next day zombies turn adjacent human beings into zombies. A zombie is adjacent to the human one block above, below, left and right. Zombie cannot cross a wall.
Find out how many days does it take to infect all human. If some human never get infected, return -1.

Input 1:
```python
mat[4][5]={{2, 1, 0, 0, 0},
           {2, 0, 2, 2, 0},
           {1, 2, 0, 0, 0},
           {0, 2, 0, 0, 0}}
```
Output: 8

Explanation:

```python
Day 1: {0, 2}, {1, 1}, {3, 0}
Day 2: {0, 3}
Day 3: {0, 4}
Day 4: {1, 4}
Day 5: {2, 4}
Day 6: {2, 3}, {3, 4}
Day 7: {2, 2}, {3, 3}
Day 8: {3, 2}
```


Input 2: 
```python
mat[3][4]={{2, 0, 0, 0},
           {2, 2, 1, 0},
           {0, 0, 2, 2}}
```
Output: -1

Explanation: {2, 0} and {2, 1} never gets infected.
