class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # def append(self, value):
    #     new_node = Node(value)
    #     temp = self.head

    #     while temp.next:
    #         temp = temp.next
        
    #     temp.next = new_node
    #     self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head 
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head == None
            self.tail == None
        return temp.value

    def prepend(self, value):
        new_node = Node(value)

        if(self.length) == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def popFirst(self):
        if(self.length) == 0:
            return None
        temp = self.head
        self.head = self.head.next

        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None

        return temp.value

    
    def insert(self, index, value):
        None
    
    def print_list(self):
        temp = self.head
        while temp.next:
            print(temp.value)
            temp = temp.next
            print("here", temp)
        print(temp.value)

        print("here", temp)


###########################################
# ll = LinkedList(40)
# # print(ll.head.value)

# ll.append(3)
# ll.append(2)
# ll.append(1)
# ll.append(6)

# ll.print_list()
# print("tail", ll.tail.value)
###########################################

ll = LinkedList(1)

ll.append(2)

ll.print_list()