# Time Complexity O(n)
# In-order traversal
# Time: ~ 40 Minutes


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.val})"

def isBST(root):
    if root is None:
        return True

    if root.left is not None and root.left.val > root.val or root.right is not None and root.right.val < root.val:
        return False
    
    left_valid = isBST(root.left)
    right_valid = isBST(root.right)

    return left_valid and right_valid




    

# Test Case 1: Single node tree
root = Node(1)
assert isBST(root) == True

# Test Case 2: BST tree
root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)
assert isBST(root) == True

# Test Case 3: Non-BST tree
root = Node(4)
root.left = Node(2)
root.left.left = Node(5)
root.left.right = Node(3)
root.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)
assert isBST(root) == False