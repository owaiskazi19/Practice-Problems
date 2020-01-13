# def bfs(graph, source):
#     visited = [False for i in range(len(adj))]
#     queue = []
#     queue.append(source)
#     visited[source] = True
#     while queue:
#         x = queue.pop(0)
#         print x
#         for i in range(graph[x]):
#             if visited[i] == False:
#                 queue.append(i)
#                 visited[i] == True




from collections import defaultdict 
  
# This class represents a directed graph 
# using adjacency list representation 
class Graph: 
  
    # Constructor 
    def __init__(self): 
  
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # Function to print a BFS of graph 
    def BFS(self, s, visited): 
        print self.graph
        # Mark all the vertices as not visited 
        
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            x = queue.pop(0)
            print x
            for i in (self.graph[x]):
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
    
    def BFSDis(self, v):
        count = 0
        visited = [False for i in range(len(self.graph))]
        print visited
        for i in range(v):
            if visited[i] == False:
                self.BFS(i, visited)
                count += 1
        print count
            

  
# Driver code 
  
# Create a graph given in 
# the above diagram 
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
g.addEdge(4,5)
g.addEdge(5,6)
g.addEdge(6,4)
  
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)") 

g.BFSDis(7) 
  