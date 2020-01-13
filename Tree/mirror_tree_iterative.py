class Solution(object):               
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = []
        if root is None:
            return True
        queue.append(root.left)
        queue.append(root.right)

        while(len(queue) >0):
            leftRoot = queue.pop(0)
            rightRoot = queue.pop(0)

            if leftRoot is None and rightRoot is None:
                continue

            if (leftRoot is None and rightRoot is not None) or (leftRoot is not None and rightRoot is None):
                return False
            
            if leftRoot.key != rightRoot.key:
                return False
            
            queue.append(leftRoot.left)
            queue.append(rightRoot.right)
            queue.append(leftRoot.right)
            queue.append(rightRoot.left)
        
        return True