
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

def search(root, val):
    if (root is None or root.val == val):e
            return root
        
    if (root.val > val):
        return search(root.left, val)
    else:
        return search(root.right, val)

def inorder(root):
    if root:
        inorder(root.left)
        print root.val
        inorder(root.right)

r = Node(50)
insert(r, Node(30))
insert(r, Node(100))
insert(r, Node(70))
inorder(r)
search(r, 30)

