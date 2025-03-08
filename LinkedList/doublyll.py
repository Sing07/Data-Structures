class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    

class DoublyLinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node


        self.length += 1

        return True
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def print_f_and_b(self):
        temp = self.head
        while temp:
            prev_node = temp.prev if temp.prev is not None else 'None'
            next_node = temp.next if temp.next is not None else 'None'
            print(f'value: {temp.value}, prev: {prev_node}, next: {next_node}')
            temp = temp.next


dll = DoublyLinkedList(1)
dll.append(2)
dll.append(3)
dll.append(4)
 
dll.print_list()
dll.print_f_and_b()