# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if root is None:
            return
        queue = []
        ans = []
        queue.append(root)
        
        while(len(queue) > 0):
            res = []
            nodeCount = len(queue) #number of nodes at a level
            while(nodeCount > 0): #Dequeue current levels node and enqueue next level nodes
                newQ = queue[0]
                res.append(newQ.val)
                queue.pop(0)
                if newQ.left is not None:
                    queue.append(newQ.left)
                if newQ.right is not None:
                    queue.append(newQ.right)
                nodeCount -= 1
            ans.append(res)
        return ans