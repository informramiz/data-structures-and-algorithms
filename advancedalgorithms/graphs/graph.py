"""
Author: Ramiz Raja
Created on: 22/01/2020
"""
from advancedalgorithms.graphs.graph_node import GraphNode


class Graph:
    def __init__(self, nodes_list=None):
        if nodes_list is None:
            nodes_list = []
        self.nodes = nodes_list

    def add_node(self, value):
        if isinstance(value, GraphNode):
            self.nodes.append(value)
        else:
            self.nodes.append(GraphNode(value))

    def add_edge(self, node1: GraphNode, node2: GraphNode):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2)
            node2.add_child(node1)

    def remove_edge(self, node1: GraphNode, node2: GraphNode):
        if node1 in self.nodes and node2 in self.nodes:
            node1.remove_child(node2)
            node2.remove_child(node1)

    def __repr__(self):
        return str([n for n in self.nodes])
