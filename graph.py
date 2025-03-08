class Graph:
    def __init__(self) -> None:
        self.adj_list = {} 

    def print(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False 
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)

    def remove_edge(self, v1, v2):
        v1.remov
    
myGraph = Graph()

myGraph.add_vertex('A')
myGraph.add_vertex('B')
myGraph.add_vertex('C')
myGraph.add_edge("A","B")
myGraph.add_edge("A","C")
myGraph.print()

# REVIEW
#removal of edge, why |E|? https://gale.udemy.com/course/data-structures-algorithms-python/learn/lecture/27237936#overview