
from collections import defaultdict

class Graph:
    def __init__(self, v):
        self.graph = defaultdict(list)
        self.vertices = v
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
    

    def topoUtil(self, s, visited, stack):
        visited[s] == True

        for i in self.graph[s]:
            if visited[i] == False:
                self.topoUtil(i, visited, stack)
        
        stack.insert(0, s)





    def topo(self):
        stack = []
        visited = [False for i in range(self.vertices)]
        print visited
        for i in range(self.vertices):
            if visited[i] == False:
                self.topoUtil(i, visited, stack)

        print stack






g = Graph(6) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print "Following is Depth First Traversal"
g.topo() 