# Time Complexity = O(n)
# Method used Pre-order tree transversal

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def copy(root):
    if root == None:
        return None
    
    dupe = Node(root.val)
    dupe.left = copy(root.left)
    dupe.right = copy(root.right)

    return dupe

# Test
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.right = Node(10)

dupe = copy(root)

print(dupe.val == 1)
print(dupe.left.val == 2)
print(dupe.right.val == 3)
print(dupe.right.right.val == 10)

