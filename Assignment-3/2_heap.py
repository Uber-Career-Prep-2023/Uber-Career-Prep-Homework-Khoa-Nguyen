import heapq

class MinHeap:

    def __init__(self):
        self.heap = []


    def top(self):
        if self.heap:
            return self.heap[0]
        
        return None

    def insert(self, x):
        return heapq.heappush(self.heap,x)

    def remove(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None

class MaxHeap:

    def __init__(self):
        self.heap = []


    def top(self):
        if self.heap:
            return -self.heap[0]
        
        return None

    def insert(self, x):
        return heapq.heappush(self.heap,-x)

    def remove(self):
        if self.heap:
            return -heapq.heappop(self.heap)
        return None




# Example usage:
min_heap = MinHeap()
min_heap.insert(3)
min_heap.insert(1)
min_heap.insert(4)

print(min_heap.top())  # Output: 1
min_heap.remove()
print(min_heap.top())  # Output: 3


# Example usage:
max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(1)
max_heap.insert(4)

print(max_heap.top())  # Output: 4
max_heap.remove()
print(max_heap.top())  # Output: 3
