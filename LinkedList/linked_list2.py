class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        self.tail.next = new_node
        self.tail = new_node

        self.length += 1
        return True


    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        new_node.next = self.head
        self.head = new_node

        self.length += 1


    def insert(self, index, value):

        if self.length < index:
            return False

        new_node = Node(value)

        temp = self.head
        
        for i in range(index - 2):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node
        self.length += 1

        return True    

    def pop(self):
        temp = self.head

        if self.length == 0:
            return None 
        
        if self.length == 1:
            popped = self.head
            self.head = None
            self.tail = None

        while temp.next.next:
            temp = temp.next

        # print("popped this: ", temp.value) # temp pointing at 2nd last node

        self.tail = temp
        popped = self.tail.next
        self.tail.next = None
        self.length -= 1

        return popped.value
    
    def reverse(self):
        temp = self.head

        self.head = self.tail
        self.tail = temp

        prev = None
        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

##################################################
# ll = LinkedList(2)
# ll.append(1)
# ll.append(2)
# ll.append(3)

# ll.prepend(88)

# ll.insert(4,99)

# ll.print_list()
# print("pop here", ll.pop())
# # ll.pop()


# print("reprint")
# ll.print_list()
##################################################

#reverse

ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)

ll.print_list()

ll.reverse()

print("after reverse")

ll.print_list()