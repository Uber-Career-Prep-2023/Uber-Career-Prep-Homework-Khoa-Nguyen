# Time Complexity O(n)
# Method: Search binary search tree (BST)
# Time: 25 min
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def floor_in_bst(root, k):
    curr = root
    floor = None
    while curr is not None:
        if curr.val == k:
            return k
        elif curr.val > k:
            curr = curr.left
        else:
            floor = curr.val
            curr = curr.right
    return floor

# Test
root = Node(8)
root.left = Node(5)
root.right = Node(12)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(10)
root.right.right = Node(14)

assert floor_in_bst(root, 6) == 5
assert floor_in_bst(root, 11) == 10
assert floor_in_bst(root, 15) == 14
assert floor_in_bst(root, 9) == 8

        





