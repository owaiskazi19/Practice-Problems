class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = []
        queue.append(root)
        while queue:
            res = []
            nodeCount = len(queue)
            while nodeCount > 0:
                node = queue.pop(0)
                res.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            
                nodeCount -= 1
        
        return res[0]