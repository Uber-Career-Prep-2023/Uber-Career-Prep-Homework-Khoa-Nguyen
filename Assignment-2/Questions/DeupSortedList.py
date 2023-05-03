# Time Complexity O(n)
# Method: Hash linked list nodes
# 20 Minutes

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

    def deleteNode(self, head, location):
        if head is None:
            return None

        if location == 0:
            return head.next

        count = 0
        curr = head

        while count != location-1:
            curr = curr.next
            count += 1

        if curr.next:
            curr.next = curr.next.next

        return head
    
    def deup_sorted_list(self,head):
        hash = set()
        counter = 0

        curr = head

        while curr:
            if curr.val in hash:
                curr.deleteNode(head, counter)
            else:
                hash.add(curr.val)
                counter +=1
            curr = curr.next


        return head
        


# create the linked list: 1 -> 1 -> 2 -> 3 -> 3 -> 4
head = Node(1, Node(1, Node(2, Node(3, Node(3, Node(4))))))
print(head)
# call the method to remove duplicates
head = head.deup_sorted_list(head)

# check that duplicates have been removed: 1 -> 2 -> 3 -> 4
print(head)