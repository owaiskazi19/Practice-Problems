from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)

    
    def DFSUtil(self, s, visited):
        visited[s] = True

        print s
        for i in self.graph[s]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def DFS(self):
        v = len(self.graph)

        visited = [False for i in range(v)]
        for i in self.graph:
            if visited[i] == False:
                self.DFSUtil(i, visited)

g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print "Following is Depth First Traversal"
g.DFS() 
