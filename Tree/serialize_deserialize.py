class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return self.helper_serialize(root, "")
    def helper_serialize(self, root, string):
        if root is None:
            string += 'None' + ','
        else:
            string += str(root.val) + ','
            string = self.helper_serialize(root.left, string)
            string = self.helper_serialize(root.right, string)
        return string

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        new_string = data.split(',')
        return self.helper_deserialize(new_string)
        
    def helper_deserialize(self, new_string):
        if new_string[0] == 'None':
            new_string.pop(0)
            return None
        else:
            node = TreeNode(new_string[0])
            new_string.pop(0)
            node.left = self.helper_deserialize(new_string)
            node.right = self.helper_deserialize(new_string)
        return node