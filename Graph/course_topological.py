class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = collections.defaultdict(set)
        outdegree = collections.defaultdict(set)
        for course,pre in prerequisites:
            outdegree[pre].add(course)
            indegree[course].add(pre)
        
        connection_removed = 0
        indegree_zero = []
        
       
        for i in range(numCourses):
            if not indegree[i]:      #not present in the indegree set
                indegree_zero.append(i)
                connection_removed += 1
        
        while indegree_zero:
            node = indegree_zero.pop()
            for x in outdegree[node]:
                indegree[x].remove(node)
                if not indegree[x]:
                    indegree_zero.append(x)
                    connection_removed += 1
        return connection_removed == numCourses
        