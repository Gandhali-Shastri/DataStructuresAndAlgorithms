# Vertex class - used to create a vertex in a graph.
#https://www.bogotobogo.com/python/python_graph_data_structures.php
class Vertex:

    def __init__(self, vertex):
        self.value = vertex
        self.connections = set()

    # __str__ method in Python represents the class objects as a string
    def __str__(self):
        return str(self.value)

    def add_neighbors(self, neighbors):
        if not neighbors:
            return

        for n in neighbors:
            if n not in self.connections:
                self.connections.add(n)

    def get_connections(self):
        return self.connections

    def get_id(self):
        return self.value
