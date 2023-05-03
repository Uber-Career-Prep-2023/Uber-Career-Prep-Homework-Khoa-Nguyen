class Node:
    def __init__ (self, val=0, next=None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        values = []
        node = self
        while node is not None:
            values.append(str(node.val))
            node = node.next
        return " <-> ".join(values)
    
    def insertAtFront(self, head, val):
        new_node = Node(val)
        new_node.next = head
        new_node.prev = head.prev

        return new_node
    
    def insertAtBack(self, head, val):
        if head is None:
            return Node(val, None, None)
        
        current = head
        while current.next is not None:
            current = current.next

        current.next = Node(val, None, current)

        return head
    
    def insertAfter(self, head, val, location):
        count = 0
        curr = head
        while count != location:
            curr = curr.next
            count += 1
        
        new_node = Node(val, curr.next, curr)
        curr.next = new_node
        return head

    def deleteFront(self, head):
        head = head.next
        head.prev = None
        return head
    
    def deleteBack(self, head):
        if head is None:
            return None

        if head.next is None:
            return None

        curr = head
        while curr.next is not None:
            curr = curr.next

        curr.prev.next = None
        curr.prev = None

        return head
    
    def deleteNode(self, head, location):
        count = 0
        curr = head

        while count != location-1:
            curr = curr.next
            count += 1


        curr.next.next.prev = curr
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
            curr.prev = temp
            prev = curr
            curr = temp
        
        return prev
    


if __name__ == "__main__":

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    # link nodes
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2

    # test insertAtFront method
    head = node1
    head = head.insertAtFront(head, 0)
    print(head)

    print("-----")

    head = Node(1)
    head = head.insertAtBack(head, 2)
    print(head)
    head = head.insertAtBack(head, 3)
    print(head)

    print("-----")

    head = Node(1)
    head = head.insertAtBack(head, 2)
    head = head.insertAtBack(head, 3)
    print(head)  # prints "1 <-> 2 <-> 3"

    # insert node after position 1 (node2)
    head = head.insertAfter(head, 4, 1)
    print(head)  # prints "1 <-> 2 <-> 4 <-> 3"

    print("-----")

    # create linked list with three nodes
    head = Node(1)
    head = head.insertAtBack(head, 2)
    head = head.insertAtBack(head, 3)
    print(head)  # prints "1 <-> 2 <-> 3"

    # delete first node (node1)
    head = head.deleteFront(head)
    print(head)  # prints "2 <-> 3"

    print("-----")

    # create linked list with three nodes
    head = Node(1)
    head = head.insertAtBack(head, 2)
    head = head.insertAtBack(head, 3)
    print(head)  # prints "1 <-> 2 <-> 3"

    # delete last node (node3)
    head = head.deleteBack(head)
    print(head)  # prints "1 <-> 2"

    print("-----")

    # create linked list with three nodes
    head = Node(1)
    head = head.insertAtBack(head, 2)
    head = head.insertAtBack(head, 3)

    print(head)  # output: 1 <-> 2 <-> 3

    head = head.deleteNode(head, 1)

    print(head)  # output: 1 <-> 3

    print("-----")

    # create linked list with three nodes
    head = Node(1)
    head = head.insertAtBack(head, 2)
    head = head.insertAtBack(head, 3)

    print(head.length(head))  # expected output: 3

    print("-----")
    
    # create the doubly linked list: 1 <-> 2 <-> 3 <-> 4
    head = Node(1)
    head = head.insertAtBack(head, 2)
    head = head.insertAtBack(head, 3)
    head = head.insertAtBack(head, 4)

    # print the original doubly linked list
    print(head)

    # reverse the doubly linked list iteratively
    head = head.reverseIterative(head)

    # print the reversed doubly linked list
    print(head)