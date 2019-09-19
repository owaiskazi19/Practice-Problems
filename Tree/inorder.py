class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        current = root
        while True:
            if current is not None:
                stack.append(current)
                current = current.left

            elif(stack):
                current = stack.pop()
                print current.key
                current = current.right