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

    def print_queue(self):
        temp = self.first

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, data):
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1


    # def dequeue(self):
    #     if self.length == 0:
    #         return None
    #     temp = self.first

    #     self.first = self.first.next
    #     temp.next = None

    #     self.length -= 1     # dont understand why not handling the self.last will not dequeue if there is 1 more item left

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None

        self.length -= 1
    

queue = Queue(4)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(1)
print("len", queue.length)


# queue.print_queue()

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()

queue.print_queue()
print("len", queue.length)
