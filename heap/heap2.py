class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index -1)  // 2
    
    def left_child(self, index):
        return index * 2 + 1
    
    def right_child(self, index):
        return index * 2 + 2

    def swap(self, v1, v2):
        self.heap[v1], self.heap[v2] = self.heap[v2], self.heap[v1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)


    def remove(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        
        self.sink_down(0)

        return max_value

    def sink_down(self, index):
        max_index = index

        while True:
            left_index = self.left_child(index)
            right_index = self.right_child(index)

            if (left_index < len(self.heap)) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index

            if (right_index < len(self.heap)) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index
                
            if max_index != index:
                self.swap(index, max_index)
                index = max_index
            else:
                return

heap = MaxHeap()
heap.insert(99)
heap.insert(72)
heap.insert(61)
heap.insert(58)

print(heap.heap)

heap.insert(100)

print(heap.heap)

heap.insert(75)

print(heap.heap)

print(heap.remove())

print(heap.heap)

