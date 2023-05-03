class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        def traverse(node):
            if node is None:
                return ''
            return f'{node.val}({traverse(node.left)},{traverse(node.right)})'
        
        return traverse(self.root)

    def insert(self, curr, val):
        if self.root is None:
            self.root = Node(val)
            return

        if val == curr.val:
            print(f"{val} is already in the tree")
            return

        if val < curr.val:
            if curr.left is None:
                curr.left = Node(val)
            else:
                self.insert(curr.left, val)

        else:
            if curr.right is None:
                curr.right = Node(val)
            else:
                self.insert(curr.right, val)

    def min(self):
        if self.root == None:
            return None
        
        curr = self.root
        while curr.left:
            curr = curr.left
        
        return curr.val
    
    def max(self):
        if self.root == None:
            return None
        
        curr = self.root
        while curr.right:
            curr = curr.right
        
        return curr.val
    
    def contains(self, val):
        if self.root == None:
            return False
        
        curr = self.root

        if curr.val == val:
            return True
        
        while curr != None:
            if curr.val < val:
                curr = curr.right
            elif curr.val > val:
                curr = curr.left
            else:
                return True
        
        return False
    
    # def delete(self, val):





if __name__ == "__main__":
    #Test For Insert
    bst = BinarySearchTree()
    bst.insert(bst.root, 5)
    bst.insert(bst.root, 2)
    bst.insert(bst.root, 3)
    bst.insert(bst.root, 7)
    bst.insert(bst.root, 1)
    bst.insert(bst.root, 9)
    print(bst)
    print("-------------------------------")

    #Test for Min
    assert bst.min() == 1, "False"
    print("Correct")
    print("-------------------------------")

    #Test for Max
    assert bst.max() == 9, "False"
    print("Correct")
    print("-------------------------------")

    print(bst.contains(1))   # True
    print(bst.contains(9))   # True
    print(bst.contains(10))   # False