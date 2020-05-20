class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.mx = 0
        def helper(root, parent, count):
            if root is None:
                return 
            if parent and parent.val + 1 == root.val:
                count += 1
            else:
                count = 1
            self.mx = max(self.mx, count)
            helper(root.left, root, count)
            helper(root.right, root,count)

        
        helper(root, None,  0)
        return self.mx