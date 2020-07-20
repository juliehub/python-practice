"""
https://leetcode.com/discuss/interview-question/436073/
You are given an undirected connected graph. 
An articulation point (or cut vertex) is defined as a vertex which, 
when removed along with associated edges, makes the graph disconnected
(or more precisely, increases the number of connected components in the graph).
The task is to find all articulation points in the given graph.

Input:

n: an int representing the total number of nodes.
m: an integer representing the number of edges in the graph.
edges: the list of pair of integers - A, B representing an edge between the nodes A and B.

Algorithm:
https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/
https://cp-algorithms.com/graph/cutpoints.html
Pick an arbitrary vertex of the graph root and run depth first search from it.
Note the following fact (which is easy to prove):

-Let's say we are in the DFS, looking through the edges starting from vertex v≠root.
If the current edge (v,to) is such that none of the vertices to or its descendants
in the DFS traversal tree has a back-edge to any of ancestors of v,
then v is an articulation point. 
Otherwise, v is not an articulation point.

-Let's consider the remaining case of v=root.
This vertex will be the point of articulation
if and only if this vertex has more than one child in the DFS tree.
"""
# Python program to find articulation points in an undirected graph 
   
from collections import defaultdict 
   
#This class represents an undirected graph  
#using adjacency list representation 
class Graph: 
   
    def __init__(self,vertices,edges): 
        self.V= vertices #No. of vertices 
        self.graph = defaultdict(list) # default dictionary to store graph 
        self.Time = 0
        
        # add edges to graph 
        for u, v in edges:
            self.graph[u].append(v) 
            self.graph[v].append(u) 
   
    '''A recursive function that find articulation points  
    using DFS traversal 
    u --> The vertex to be visited next 
    visited[] --> keeps tract of visited vertices 
    disc[] --> Stores discovery times of visited vertices 
    parent[] --> Stores parent vertices in DFS tree 
    ap[] --> Store articulation points'''
    def APUtil(self,u, visited, ap, parent, low, disc): 
  
        #Count of children in current node  
        children =0
  
        # Mark the current node as visited and print it 
        visited[u]= True
  
        # Initialize discovery time and low value 
        disc[u] = self.Time 
        low[u] = self.Time 
        self.Time += 1
  
        #Recur for all the vertices adjacent to this vertex 
        for v in self.graph[u]: 
            # If v is not visited yet, then make it a child of u 
            # in DFS tree and recur for it 
            if visited[v] == False : 
                parent[v] = u 
                children += 1
                self.APUtil(v, visited, ap, parent, low, disc) 
  
                # Check if the subtree rooted with v has a connection to 
                # one of the ancestors of u 
                low[u] = min(low[u], low[v]) 
  
                # u is an articulation point in following cases 
                # (1) u is root of DFS tree and has two or more chilren. 
                if parent[u] == -1 and children > 1: 
                    ap[u] = True
  
                #(2) If u is not root and low value of one of its child is more 
                # than discovery value of u. 
                if parent[u] != -1 and low[v] >= disc[u]: 
                    ap[u] = True    
                      
                # Update low value of u for parent function calls     
            elif v != parent[u]:  
                low[u] = min(low[u], disc[v]) 
  
  
    #The function to do DFS traversal. It uses recursive APUtil() 
    def AP(self): 
        """
        # Returns: a list of integers representing the critical nodes.
        """
        # Mark all the vertices as not visited  
        # and Initialize parent and visited,  
        # and ap(articulation point) arrays 
        visited = [False] * (self.V) 
        disc = [float("Inf")] * (self.V) 
        low = [float("Inf")] * (self.V) 
        parent = [-1] * (self.V) 
        ap = [False] * (self.V) #To store articulation points 
  
        # Call the recursive helper function 
        # to find articulation points 
        # in DFS tree rooted with vertex 'i' 
        for i in range(self.V): 
            if visited[i] == False: 
                self.APUtil(i, visited, ap, parent, low, disc) 
  
        a_node=[]
        for index, value in enumerate (ap): 
            if value == True:
                a_node.append(index)
        
        return a_node

n = 7
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
#Output: [2, 3, 5]
    
#n = 6
#edges = [[1, 2], [1, 3], [2, 3], [2, 4], [2, 5], [4, 6], [5, 6]]

#n = 9
#edges = [[1, 2], [1, 3], [2, 3], [3, 4], [3, 6], [4, 5], [6, 7], [6, 9], [7, 8], [8, 9]]

g1 = Graph(n,edges)             
print("\nArticulation points in first graph ",g1.AP())
