class Solution(object):
    def dfs(self, board, i, j):
        if not 0 <= i < len(board) or not 0 <= j < len(board[i]) or board[i][j]!='O':
            return
        
        board[i][j] = 'D'
        self.dfs(board, i + 1, j)
        self.dfs(board, i - 1, j)
        self.dfs(board, i, j - 1)
        self.dfs(board, i, j + 1)
        
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if board is None or len(board) == 0:
            return 0
        
        for i in range(0,len(board)):
            for j in range(0, len(board[i])):
                if (i in [0, len(board)-1] or j in [0, len(board[0])-1]) and board[i][j] == 'O':
                    self.dfs(board, i, j)
        
        
        for i in range(0,len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == 'D':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        return board