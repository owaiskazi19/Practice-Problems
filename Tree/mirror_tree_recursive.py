class Solution(object):
    def isMirror(root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is not None and root2 is not None:
            if root1.key == root2.key:
                return (isMirror(root1.left, root2,right) and isMirror(root1.right, root2.left))
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
       isMirror(root,root)
            

