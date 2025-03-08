class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

bst = BinarySearchTree()
bst.insert(2)
bst.insert(1)
bst.insert(3)
bst.insert(4)
bst.insert(7)
bst.insert(9)

print(bst.root.value)
print(bst.root.left.value)
print(bst.root.right.value)

print(bst.contains(2))
print(bst.contains(1))
print(bst.contains(3))
print(bst.contains(4))
print(bst.contains(5))
print(bst.contains(6))
print(bst.contains(8))
