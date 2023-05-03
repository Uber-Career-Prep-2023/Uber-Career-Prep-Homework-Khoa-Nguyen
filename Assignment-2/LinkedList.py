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
    
    def insertAtFront(self, head, val):
        new_node = Node(val)
        new_node.next = head
        return new_node

    def insertAtBack(self, head, val):
        if head is None:
            return Node(val, None)
        
        current = head
        while current.next is not None:
            current = current.next
        current.next = Node(val, None)

        return head

    def insertAfter(self, head, val, location):
        count = 0

        while count != location:
            head = head.next
            count += 1

        new_node = Node(val,head.next)
        head.next = new_node

        return head
    
    def deleteFront(self, head):
        head = head.next
        return head
    
    def deleteBack(self, head):
        if head is None:
            return None
        
        if head.next is None:
            return None
            
        curr = head
        while curr.next.next is not None:
            curr = curr.next
            
        curr.next = None
        return head
    
    def deleteNode(self, head, location):
        count = 0
        curr = head

        while count != location-1:
            curr = curr.next
            count += 1

        curr.next = curr.next.next

        return head
    
    def length(self, head):
        count = 0

        if head is None: 
            return 0
        
        else:
            while head is not None:
                head = head.next
                count += 1

        return count

    def reverseIterative(self,head):
        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
    
    # def reverseRecursive(self,head):
    #     if (head is None) or (head.next is None):
    #         return head
        

    




if __name__ == "__main__":
    # create some nodes to test the functions
    head = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    head.next = node2
    node2.next = node3
    
    # test insertAtFront
    head = head.insertAtFront(head, 0)
    while head is not None:
        print(head.val)
        head = head.next
    
    print("-----")
        
    # test insertAtBack
    head = Node(1)
    head = head.insertAtBack(head, 2)
    head = head.insertAtBack(head, 3)
    while head is not None:
        print(head.val)
        head = head.next
    print("-----")
        
    # test insertAfter
    head = Node(1)
    head.insertAfter(head, 2, 0)
    head.insertAfter(head, 3, 1)
    while head is not None:
        print(head.val)
        head = head.next
    print("-----")

    # create some nodes to test the functions
    head = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    head.next = node2
    node2.next = node3

    # test deleteFront
    print("Before deletion:")
    node = head
    while node is not None:
        print(node.val)
        node = node.next

    head = head.deleteFront(head)

    print("After deletion:")
    node = head
    while node is not None:
        print(node.val)
        node = node.next

    print("-----")

    # create some nodes to test the functions
    head = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    head.next = node2
    node2.next = node3

    # test deleteBack
    head = head.deleteBack(head)
    while head is not None:
        print(head.val)
        head = head.next
    print("-----")

    # Create linked list
    head = Node(1)
    head = head.insertAtBack(head, 2)
    head = head.insertAtBack(head, 3)
    head = head.insertAtBack(head, 4)

    # Delete node at location 2 (value 3)
    head = head.deleteNode(head, 2)

    # Expected output: 1 -> 2 -> 4
    print(head)
    print("-----")

    # Define test linked list
    head = Node(1)
    head = head.insertAtBack(head, 2)
    head = head.insertAtBack(head, 3)

    # Call length function and print result
    print(head.length(head)) # expected output: 3
    print("-----")

    # create linked list 1 -> 2 -> 3 -> 4 -> 5
    node5 = Node(5, None)
    node4 = Node(4, node5)
    node3 = Node(3, node4)
    node2 = Node(2, node3)
    node1 = Node(1, node2)

    # reverse the list
    new_head = node1.reverseIterative(node1)

    # print the reversed list
    while new_head:
        print(new_head.val)
        new_head = new_head.next
    print("-----")


