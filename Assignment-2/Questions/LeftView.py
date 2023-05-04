# Time Complexity O(n)
# Method: Level Order Binary Tree Traversal
# Time ~ 40 Min
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def left_view(root):
    result = []
    level = []
    queue = [root]
    while queue != [] and root is not None:
        for node in queue:
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
        result.append(queue[0].val)
        queue = level
        level = []
    return result


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
assert left_view(root) == [1, 2, 4]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.left.right = Node(6)
root.right.left.right.left = Node(7)
assert left_view(root) == [1, 2, 4, 6, 7]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(6)
root.right.left = Node(7)
root.right.right = Node(8)
assert left_view(root) == [1, 2, 4, 6]


