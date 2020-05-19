class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return 1 + self.maxDepth(root.right)
        if root.right is None:
            return 1 + self.maxDepth(root.left)
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))