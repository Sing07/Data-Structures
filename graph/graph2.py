class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def print_graph(self):
        for v,e in self.adj_list.items():
            print(v, e)

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False


# graph = Graph()

# graph.add_vertex(1)
# graph.add_vertex(2)

# graph.add_edge(1,2) 

# graph.print_graph()

# graph.remove_edge(1,2)
# graph.print_graph()

graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")

graph.print_graph()

graph.add_edge("A", "B")

graph.print_graph()

graph.add_vertex("C")

graph.add_edge("C", "A")

graph.print_graph()

