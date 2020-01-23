"""
Author: Ramiz Raja
Created on: 23/01/2020
"""

class Edge(object):
    def __init__(self, node, distance):
        self.node = node
        self.distance = distance


class GraphNode(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

    def add_edge(self, node, distance):
        self.edges.append(Edge(node, distance))

    def remove_edge(self, edge):
        if edge in self.edges:
            self.edges.remove(edge)

    def remove_node_edge(self, node):
        node_edge = None
        for edge in self.edges:
            if edge.node == node:
                node_edge = edge
                break

        if node_edge:
            self.edges.remove(node_edge)


class Graph(object):
    def __init__(self, nodes_list=None):
        if nodes_list is None:
            nodes_list = []
        self.nodes = nodes_list

    def is_empty(self):
        return len(self.nodes) == 0

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, node1: GraphNode, node2: GraphNode, distance):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_edge(node2, distance)
            node2.add_edge(node1, distance)

    def remove_edge(self, node1: GraphNode, node2: GraphNode):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_node_edge(node2)
            node2.remove_node_edge(node1)


