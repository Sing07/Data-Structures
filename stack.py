class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value) -> None:
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
        new_node.next = self.top
        self.top = new_node
        self.height += 1

    def num(self):
        print(self.height)


stack = Stack(4)
stack.push(3)
stack.push(2)
stack.push(1)
stack.push(1)
stack.print_stack()
stack.num()
