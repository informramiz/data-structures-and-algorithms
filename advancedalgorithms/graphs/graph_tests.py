"""
Author: Ramiz Raja
Created on: 22/01/2020
"""
from advancedalgorithms.graphs.graph import *
from asserts.asserts import assert_


def tests():
    graph = Graph()
    nodeA = GraphNode('A')
    nodeB = GraphNode("B")
    nodeC = GraphNode("C")

    graph.add_node(nodeA)
    graph.add_node(nodeB)
    graph.add_node(nodeC)

    graph.add_edge(nodeA, nodeC)
    graph.add_edge(nodeB, nodeC)

    assert_(expected=['A', 'C', 'B'], actual=graph.BFS_traversal())
    assert_(expected=nodeB, actual=graph.BFS_search('B'))


tests()