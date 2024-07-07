from Graph.Graph import Graph


#https://www.bogotobogo.com/python/python_graph_data_structures.php
if __name__ == '__main__':
    g = Graph()

    a = g.add_vertex("A")
    b = g.add_vertex("B")
    c = g.add_vertex("C")
    d = g.add_vertex("D")

    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "E")
    g.add_edge("D", "F")

    # for v in g:
    #     for w in v.get_connections():
    #         vid = v.get_id()
    #         wid = w.get_id()
    #         print('( %s , %s, %3d)' % (vid, wid, v.get_weight(w)))


    print("Neighbors in graph")
    for v in g:
        print(v.value, "-->", v.get_connections())
