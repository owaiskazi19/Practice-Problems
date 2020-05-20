class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        def helper(root):
            if root:
                if root.left and not root.left.left and not root.left.right:
                    self.sum += root.left.val
                helper(root.left)
                helper(root.right)
        helper(root)
        return self.sum
        