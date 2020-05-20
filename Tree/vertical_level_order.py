from collections import defaultdict
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return
        
        queue = []
    
        res = defaultdict(list)
        
        hd = 0
        
        queue.append((root,hd))
        while queue:
            nodeCount = len(queue)
            while nodeCount > 0:
                node, hd_new = queue.pop(0)
                res[hd_new].append(node.val)
                if node.left is not None:
                    queue.append((node.left, hd_new - 1))
                if node.right is not None:
                    queue.append((node.right, hd_new + 1))
                nodeCount -= 1
        
        return [res[x] for x in sorted(res.keys())]
        