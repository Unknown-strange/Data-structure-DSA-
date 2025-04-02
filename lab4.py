#1825622
#Nyarko Prince Edwin

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_nodes(root):
    """Counts the total number of nodes in a binary tree."""
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def compute_depth(root):
    """Computes the depth (height) of a binary tree."""
    if root is None:
        return 0
    return 1 + max(compute_depth(root.left), compute_depth(root.right))


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Number of nodes:", count_nodes(root))  
print("Depth of tree:", compute_depth(root))

