class Solution(object):
    def dfs(self, grid, i , j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0':
            return 0
        

        grid[i][j] = '0'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)
        
        return 1
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if grid is None or len(grid) == 0:
            return 0
        
        numIsland = 0
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                    numIsland += self.dfs(grid, i , j)
        
        return numIsland
        
        