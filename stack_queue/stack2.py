class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class Stack:
    def __init__(self, value):
        self.head = Node(value)
        self.top = self.head
        self.height = 1

    def push(self, value):
        new_node = Node(value)

        if self.height == 0:
            self.top = new_node
            self.height += 1
            return True
        
        new_node.next = self.top
        self.top = new_node
        self.height += 1
        return True
    
    def pop(self):

        if self.height == 0:
            return None

        popped = self.top
        self.top = self.top.next
        self.height -= 1
        return popped
    
    def print_stack(self):
        temp = self.top

        while temp:
            print(temp.value)
            temp = temp.next

stack = Stack(4)
stack.push(3)
stack.push(2)
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()


# stack.print_stack()

print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)

print("after pop")
stack.print_stack()

