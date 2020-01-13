class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
def printLevelOrder(root):
    h = height(root)
    for i in range(0, h+1):
        printGivenOrder(root, i)

def printGivenOrder(root, level):
    if root is None:
        return
    if level == 1:
        print root.val
    elif level > 1:
        printGivenOrder(root.left, level - 1)
        printGivenOrder(root.right, level -1)

def height(root):
    if root is None:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)
    if lheight > rheight:
        return lheight + 1
    else:
        return rheight + 1

root = Node(50)
root.left = Node(40)
root.right = Node(30)
root.left.left= Node(20)
printLevelOrder(root)