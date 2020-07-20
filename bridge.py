"""
https://leetcode.com/discuss/interview-question/372581

Given an underected connected graph with n nodes labeled 1..n. 
A bridge (cut edge) is defined as an edge which, when removed, 
makes the graph disconnected (or more precisely, increases the number of connected components in the graph).
Equivalently, an edge is a bridge if and only if it is not contained in any cycle. 
The task is to find all bridges in the given graph. Output an empty list if there are no bridges.

Input:

n, an int representing the total number of nodes.
edges, a list of pairs of integers representing the nodes connected by an edge.

Solution:

A python solution which find Bridges (Edges that when removed, increase the number of components)

Key Idea - For any edge parent -> child, if an edge exists between child->ancestor
where ancestor is an ancestor of the vertex parent, this is not a bridge edge.
In addition to the usual visited set during a DFS, you also keep track of discovered,
which is the time when a particular node was first first seen.
low is the minimum of the time the node was first seen and all its neighbors (expect for the parent) were first seen.
"""
from typing import List
from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        # Build the graph first 
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        # Required for book keeping 
        # Regular DFS visited set 
        visited = set()
        # Lowest link needed to find backedges
        low = {}
        discovered = defaultdict(int)
        # Edges that will break the connected components
        bridges = []

        def dfs(vertex, parent, time):
            visited.add(vertex)
            low[vertex] = time
            discovered[vertex] = time
            for child in graph[vertex]:
                if child == parent:
                    continue
                if child not in visited:
                    dfs(child, vertex, time+1)
                    # Update the lowest link value
                    # The lowest link of a node, is either its own value or the lowest link of all its neighbors
                    # that are not the parent node
                    low[vertex] = min(low[vertex], low[child])
                    if discovered[vertex] < low[child]:
                        bridges.append([vertex, child])
                else:
                    low[vertex] = min(low[vertex], discovered[child])


        # Run DFS on the nodes at the top level
        for i in range(n):
            if i not in visited:
                dfs(i, None, 0)

        return bridges

n = 7
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
s=Solution()
print("Bridges:",s.criticalConnections(n,edges))


#numNodes = 5
#edges = [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]
#s=Solution()
#print("Bridges:",s.criticalConnections(n,edges))


#n = 6
#edges = [[1, 2], [1, 3], [2, 3], [2, 4], [2, 5], [4, 6], [5, 6]]
#s=Solution()
#print("Bridges:",s.criticalConnections(n,edges))
