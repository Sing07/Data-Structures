class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root    
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
                return True
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right



my_tree = BST()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)
print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)


# create new_node
# if root = none, then insert new_node
# while node != None
#   if(new_node.val < node)
#       insert node.left
#   else insert node.right
#   if new_node.val = node.val:
#       return False        