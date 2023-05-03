# Time Complexity: O(n)
# Method: Linked list fixed-distance three-pointer, Simultaneous iteration three-pointer
# Time 25 Minutes
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
    
    
    def move_nth_last_to_front(self, head, nth):
        prev = None
        behind = head
        curr = head

        for i in range(nth-1):
            curr = curr.next

        while curr.next:
            curr = curr.next
            prev = behind
            behind = behind.next
        
        prev.next = behind.next
        behind.next = head
        head = behind

        return head


    
head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10))))))))))
print(head)

# Move the 2nd last node (value 4) to the front of the list
head = Node().move_nth_last_to_front(head, 2)

# Check that the linked list has been modified correctly
print(head) # Expected: 4 -> 1 -> 2 -> 3 -> 5




