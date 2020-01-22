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
    nodeAA = GraphNode("AA")

    graph.add_node(nodeA)
    graph.add_node(nodeAA)
    graph.add_node(nodeB)
    graph.add_node(nodeC)

    graph.add_edge(nodeA, nodeC)
    graph.add_edge(nodeA, nodeAA)
    graph.add_edge(nodeC, nodeB)

    assert_(expected=['A', 'C', "AA", 'B'], actual=graph.BFS_traversal())
    assert_(expected=nodeB, actual=graph.BFS_search('B'))

    assert_(expected=["A", "C", "B", "AA"], actual=graph.DFS_traversal_iterative())
    assert_(expected=["A", "C", "B", "AA"], actual=graph.DFS_traversal_recursive())

    assert_(expected=nodeB, actual=graph.DFS_search_iterative('B'))
    assert_(expected=nodeB, actual=graph.DFS_search_recursive('B'))


tests()
