"""
Author: Ramiz Raja
Created on: 22/01/2020
"""
from advancedalgorithms.graphs.graph import *


def tests():
    graph = Graph()
    node1 = GraphNode('A')
    node2 = GraphNode("B")

    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_edge(node1, node2)

    print(graph)


tests()