# Time Complexity O(n)

class Node:
    def __init__ (self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        values = []
        node = self
        while node is not None:
            values.append(node.val)
            node = node.next
        return " -> ".join(str(val) for val in values)
    
    def isPalindrome(self, head):
        arr = []
        
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        if arr == arr[::-1]:
            return True
        
        return False
    
# create the linked list: 1 -> 2 -> 3 -> 2 -> 1
head = Node(1, Node(2, Node(3, Node(2, Node(1)))))

# call the method to check if it is a palindrome

print(head.isPalindrome(head)) #Expected True

# create the linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))

# call the method to check if it is a palindrome
print(head.isPalindrome(head)) #Expected False