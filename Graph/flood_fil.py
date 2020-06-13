class Solution(object):
    def dfs(self, image, i , j, color, newColor):
        if i < 0 or i >= len(image) or j < 0 or j >= len(image[i])  or image[i][j] != color:
            return
        if image[i][j] == color:
            image[i][j] = newColor
        print i,j, image
        self.dfs(image, i - 1, j, color, newColor)
        self.dfs(image, i + 1, j , color, newColor)
        self.dfs(image, i, j - 1, color, newColor)
        self.dfs(image, i, j + 1, color, newColor)
        
        
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        color = image[sr][sc]
        if color == newColor:
            return image
        
       
        self.dfs(image, sr , sc, color, newColor)
        return image