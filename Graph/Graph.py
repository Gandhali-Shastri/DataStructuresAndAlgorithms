# Graph class - used to create a graph by adding vertices and edges
from Vertex import Vertex


#https://www.bogotobogo.com/python/python_graph_data_structures.php
class Graph:
    def __init__(self):
        self.vertices = {}
        self.vertex_count = 0

    # The __iter__() function returns an iterator for the given object
    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, v):
        self.vertex_count += 1
        new_vertex = Vertex(v)
        self.vertices[v] = new_vertex

    def add_edge(self, source, destination):
        # create new vertex if it doesn't exist
        if source not in self.vertices:
            self.add_vertex(source)

        # create new vertex if it doesn't exist
        if destination not in self.vertices:
            self.add_vertex(destination)

        self.vertices[source].add_neighbors(destination)

    def get_vertex_count(self):
        return self.vertex_count

    def get_vertex(self, v):
        if v in self.vertices:
            return self.vertices[v]
        else:
            print("Vertex doesn't exist in graph!")

    def get_vertices(self):
        return self.vertices.keys()
