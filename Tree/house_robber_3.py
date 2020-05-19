class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.helper(root))
        
    def helper(self,node):
        if not node:
            return (0,0)
        
        l_pick, l_nopick = self.helper(node.left)
        r_pick, r_nopick = self.helper(node.right)
        
        return node.val + l_nopick + r_nopick, max(l_pick, l_nopick) + max(r_pick, r_nopick)