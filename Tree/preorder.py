class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return 
        
        stack = []
        ans = []
        stack.append(root)
        
        while len(stack) > 0:
            node = stack.pop()
            ans.append(node.val)
            
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return ans