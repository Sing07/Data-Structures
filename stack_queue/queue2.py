class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    
    def enqueue(self, value):
        new_node = Node(value)
        
        if self.length == 0:
            self.first = new_node
            self.last = new_node
            return True
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True
    
    def dequeue(self):
        if self.length == 0:
            return None

        if self.length == 1:
            self.first = None
            self.last = None
            temp = self.first
        else:
            temp = self.first 
            self.first = self.first.next
        self.length -= 1
        return temp
        
    
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
        

queue = Queue(4)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(1)
print("len", queue.length)
# print("priting", queue.print_queue())
# print(queue.print_queue(), "priting")
queue.print_queue()
print("len:", queue.length)
print("now dequeing:")

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.print_queue()
print("len:", queue.length)


# # queue.print_queue()

# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()

# queue.print_queue()
# print("len", queue.length)
