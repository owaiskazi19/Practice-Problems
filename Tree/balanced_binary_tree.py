class Solution(object):
    def checkHeight(self,root):
        if root is None:
            return 0
        return 1 + max(self.checkHeight(root.left),  self.checkHeight(root.right))
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        lh = self.checkHeight(root.left)
        rh = self.checkHeight(root.right)
        
        height = abs(lh - rh)
        
        
        if height <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False