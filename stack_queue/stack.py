class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top

        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, data):
        new_node = Node(data)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
    
    def pop(self):

        if self.height == 0:
            return None
        
        temp = self.top
        self.top = self.top.next
        self.height -= 1
        return temp

stack = Stack(4)
stack.push(3)
stack.push(2)
stack.pop()
stack.pop()
stack.pop()
stack.pop()


stack.print_stack()

