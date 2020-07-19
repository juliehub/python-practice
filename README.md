# python-practice
This repository contains simple coding problems and solutions written in Python

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
Install [Python 3](https://www.python.org/downloads/) or use your favourite IDE

## How to run .py file
The most basic and the easy way to run Python scripts is by using the python command.
You need to open a command-line and type the word python followed by the path to your script file, like this:
```
python merging_ranges.py
```
It is useful to save the output in a different file for later analysis.
```
python merging_ranges.py > output.txt
```

## List of problems
### Problem 1: Merging Ranges (Sorting)
Your company built an in-house calendar tool called HiCal.
You want to add a feature to see the times in a day when everyone is available.
* Problem statement: [merging_ranges.md](https://github.com/juliehub/python-practice/blob/master/merging_ranges.md)
* Sample solution: [merging_ranges.py](https://github.com/juliehub/python-practice/blob/master/merging_ranges.py)

### Problem 2: Making Change (Dynamic Programming)
Your quirky boss collects rare, old coins...
* Problem statement: [change_making.md](https://github.com/juliehub/python-practice/blob/master/change_making.md)
* Sample solution: [change_making.py](https://github.com/juliehub/python-practice/blob/master/change_making.py)

### Problem 3: Binary Gap (Iterations)
Find longest sequence of zeros in binary representation of an integer.
* Problem statement: [binary_gap.md](https://github.com/juliehub/python-practice/blob/master/binary_gap.md)
* Sample solution: [binary_gap.py](https://github.com/juliehub/python-practice/blob/master/binary_gap.py)

### Problem 4: Cyclic Rotation (Arrays)
Rotate an array to the right by a given number of steps.
* Problem statement: [cyclic_rotation.md](https://github.com/juliehub/python-practice/blob/master/cyclic_rotation.md)
* Sample solution: [cyclic_rotation.py](https://github.com/juliehub/python-practice/blob/master/cyclic_rotation.py)

### Problem 5: Rectangular Love (Rectangle Overlap)
A crack team of love scientists from OkEros (a hot new dating site) have devised a way to represent dating profiles as rectangles on a two-dimensional plane.
* Problem statement: [rectangular_love.md](https://github.com/juliehub/python-practice/blob/master/rectangular_love.md)
* Sample solution: [rectangular_love.py](https://github.com/juliehub/python-practice/blob/master/rectangular_love.py)


### Problem 6: Highest Product of 3 (List, Time Complexity)
Given a list of integers, find the highest product you can get from three of the integers.
* Problem statement: [highest_product.md](https://github.com/juliehub/python-practice/blob/master/highest_product.md)
* Sample solution: [highest_product.py](https://github.com/juliehub/python-practice/blob/master/highest_product.py)


### Problem 7: Largest Stack (Stacks, Time Complexity)
You want to be able to access the largest element in a stack
* Problem statement: [largest_stack.md](https://github.com/juliehub/python-practice/blob/master/largest_stack.md)
* Sample solution: [largest_stack.py](https://github.com/juliehub/python-practice/blob/master/largest_stack.py)


### Problem 8: Stolen Breakfast Drone (Dictionaries)
Your company delivers breakfast via autonomous quadcopter drones. And something mysterious has happened.
* Problem statement: [drone.md](https://github.com/juliehub/python-practice/blob/master/drone.md)
* Sample solution: [drone.py](https://github.com/juliehub/python-practice/blob/master/drone.py)


### Problem 9: Simulate a 5-Sided Die Using a 7-Sided Die (Mod Operation)
You have a function rand7() that generates a random integer from 1 to 7.
Use it to write a function rand5() that generates a random integer from 1 to 5.
* Problem statement: [rand5.md](https://github.com/juliehub/python-practice/blob/master/rand5.md)
* Sample solution: [rand5.py](https://github.com/juliehub/python-practice/blob/master/rand5.py)


### Problem 10: Writing a uniform shuffle (NOT DONE YET)
Write a function for doing an in-place shuffle of a list.
Use it to write a function rand5() that generates a random integer from 1 to 5.
* Problem statement: [shuffle.md](https://github.com/juliehub/python-practice/blob/master/shuffle.md)
* Sample solution: [shuffle.py](https://github.com/juliehub/python-practice/blob/master/shuffle.py)

### Problem 11: Swapping elements (Counting elements)
Write a function to check whether there is a swap operation which can be performed on these
arrays in such a way that the sum of elements in array A equals the sum of elements in
array B after the swap.
* Problem statement: [swap.md](https://github.com/juliehub/python-practice/blob/master/swap.md)
* Sample solution: [swap.py](https://github.com/juliehub/python-practice/blob/master/swap.py)

### Problem 12: Mushroom pickers (Prefix sums)
Write a function to calculate the maximum number of mushrooms that the mushroom picker can collect in m moves.
* Problem statement: [mushroom.md](https://github.com/juliehub/python-practice/blob/master/mushroom.md)
* Sample solution: [mushroom.py](https://github.com/juliehub/python-practice/blob/master/mushroom.py)

### Problem 13: Max Slice Problem
Write a function to return the maximum sum of a slice in the array.
* Problem statement: [max_slice.md](https://github.com/juliehub/python-practice/blob/master/max_slice.md)
* Sample solution: [max_slice.py](https://github.com/juliehub/python-practice/blob/master/max_slice.py)

### Problem 14: Top K Frequently Mentioned Keywords (Heap)
Given a list of reviews, a list of keywords and an integer k. Find the most popular k keywords in order of most to least frequently mentioned.
* Problem statement: [topKFrequent.md](https://github.com/juliehub/python-practice/blob/master/topKFrequent.md)
* Sample solution: [topKFrequent.py](https://github.com/juliehub/python-practice/blob/master/topKFrequent.py)

### Problem 15: Zombie in a matrix (Breadth First Search, Graph)
Given a 2D grid, each cell is either a zombie 1 or a human 0. Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour.
Find out how many hours does it take to infect all humans?
* Problem statement: [zombie.md](https://github.com/juliehub/python-practice/blob/master/zombie.md)
* Sample solution: [zombie.py](https://github.com/juliehub/python-practice/blob/master/zombie.py)

### Problem 16: Product Suggestions (Trie and Sort)
Given an array of strings products and a string searchWord.
We want to design a system that suggests at most three product names from products after each character of searchWord is typed.
Suggested products should have common prefix with the searchWord.
If there are more than three products with a common prefix return the three lexicographically minimums products.

### Problem 17: Critical Routers (Depth First Search)
You are given an undirected connected graph. An articulation point (or cut vertex) is defined as a vertex which, when removed along with associated edges, makes the graph disconnected (or more precisely, increases the number of connected components in the graph). The task is to find all articulation points in the given graph.

Return list of lists of the suggested products after each character of searchWord is typed. 

* Problem statement: [routers.md](https://github.com/juliehub/python-practice/blob/master/routers.md)
* Sample solution: [routers.py](https://github.com/juliehub/python-practice/blob/master/routers.py)

## Authors

* **Julie** - [Julie Github Repository](https://github.com/juliehub)

## Acknowledgments

* Feel free to make a clone or a pull request :)
