class BinarySearchTree:
    def __init__(self):
        self.current_node = None
        
    def __r_contains(self, current_node, value):
        if current_node == None: 
            return False
        if current_node == value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)