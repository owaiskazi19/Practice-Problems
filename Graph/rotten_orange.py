class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = []
        count = 0
        res = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    count += 1
        
        
        if count == 0:
            return 0
        
        while queue:
            if count == 0:
                return res
            res += 1
            for k in range(0,len(queue)):
                row, col = queue.pop(0)
                if row - 1 >= 0 and grid[row-1][col] == 1:
                    grid[row-1][col] = 2
                    queue.append((row-1,col))
                    count -= 1
                if row + 1 < len(grid) and grid[row+1][col] == 1:
                    grid[row+1][col] = 2
                    queue.append((row+1,col))
                    count -= 1
                if col - 1 >= 0 and grid[row][col-1] == 1:
                    grid[row][col-1] = 2
                    queue.append((row,col-1))
                    count -= 1
                if col + 1 < len(grid[row]) and grid[row][col+1] == 1:
                    grid[row][col+1] = 2
                    queue.append((row,col+1))
                    count -= 1
        return -1
                    