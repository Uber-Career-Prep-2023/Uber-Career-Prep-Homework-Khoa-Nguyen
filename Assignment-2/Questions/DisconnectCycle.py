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
    
    def disconnect_cycle(self, head):
        arr = []

        curr = head
        
        while curr:
            arr.append(curr.val)

            if curr.next is None or curr.next.val not in arr:
                curr = curr.next

            else:
                curr.next = None
        
        return head
    
# Create the linked list: 1 -> 2 -> 3 -> 4 -> 2 (creates a cycle)
head = Node(1, Node(2, Node(3, Node(4))))
head.next.next.next.next = head.next

# Call the method to disconnect the cycle
head = head.disconnect_cycle(head)
print(head) #Expected 1 -> 2 -> 3 -> 4
