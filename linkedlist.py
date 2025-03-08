class node:
    def __init__(self, data = None) -> None:
        self.data = data
        self.next = None
    
class linked_list:
    def __init__(self) -> None:
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def display(self):
        cur = self.head
        elem = []
        while cur.next != None:
            cur = cur.next
            elem.append(cur.data)
        print(elem)

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            cur = cur.next
            total += 1
        return total
    
    def remove(self, index):
        if index < 0 or index > self.length():
            print("index out of bound!")
        
        cur = self.head
        cur_index = 0

        while True:
            prev_node = cur
            cur = cur.next
            if index == cur_index:
                prev_node.next = cur.next
                return
            cur_index +=1

        


l = linked_list()
l.append(1)
l.append(2)
l.append(12)
l.append(44)
l.append(3)
l.append(3)

l.display()
print(l.length())

l.remove(2)
l.display()

