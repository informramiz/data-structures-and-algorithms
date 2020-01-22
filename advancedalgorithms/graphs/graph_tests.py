"""
Author: Ramiz Raja
Created on: 22/01/2020
"""
from advancedalgorithms.graphs.graph import *
from asserts.asserts import assert_


def tests():
    graph = Graph()
    node1 = GraphNode('A')
    node2 = GraphNode("B")
    node3 = GraphNode("C")

    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_node(node3)

    graph.add_edge(node1, node3)
    graph.add_edge(node2, node3)

    assert_(expected=['A', 'C', 'B'], actual=graph.BFS_traversal())


tests()