"""
Author: Ramiz Raja
Created on: 23/01/2020
"""
from asserts.asserts import assert_
from advancedalgorithms.graphs.dijkstrasalgorithm.dijkstra_algorithm import *


def tests():
    node_u = GraphNode('U')
    node_d = GraphNode('D')
    node_a = GraphNode('A')
    node_c = GraphNode('C')
    node_i = GraphNode('I')
    node_t = GraphNode('T')
    node_y = GraphNode('Y')

    graph = Graph([node_u, node_d, node_a, node_c, node_i, node_t, node_y])
    graph.add_edge(node_u, node_a, 4)
    graph.add_edge(node_u, node_c, 6)
    graph.add_edge(node_u, node_d, 3)
    graph.add_edge(node_d, node_c, 4)
    graph.add_edge(node_a, node_i, 7)
    graph.add_edge(node_c, node_i, 4)
    graph.add_edge(node_c, node_t, 5)
    graph.add_edge(node_i, node_y, 4)
    graph.add_edge(node_t, node_y, 5)

    # Test-1
    start_node = node_u
    end_node = node_y
    output = dijkstra(start_node, end_node)
    end_node_value = None
    if end_node is not None:
        end_node_value = end_node.value
    print('Shortest Distance of ({} --> {}) is {} and path is {}'
          .format(start_node.value, end_node_value, output[1], output[0]))
    assert_(expected=(['U', 'C', 'I', 'Y'], 14), actual=output)

    # Test-2
    start_node = node_u
    end_node = None
    output = dijkstra(start_node, end_node)
    end_node_value = None
    if end_node is not None:
        end_node_value = end_node.value
    print('Shortest Distance of ({} --> {}) is {} and path is {}'
          .format(start_node.value, end_node_value, output[1], output[0]))
    assert_(expected=(['U', 'C', 'I', 'Y'], 14), actual=output)


tests()