class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue = []
        ans = []
        count = 0
        queue.append(root)
        
        while queue:
            nodeCount = len(queue)
            count += 1
            while nodeCount > 0:
                node = queue.pop(0)
                
                if node.left is None and node.right is None:
                    ans.append(count)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                nodeCount -= 1
        
        return max(ans)