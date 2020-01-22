"""
Author: Ramiz Raja
Created on: 22/01/2020
"""
from advancedalgorithms.graphs.graph_node import GraphNode
import collections


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

    def BFS_traversal(self):
        if len(self.nodes) == 0:
            return []

        queue = []
        visited_nodes_order = []
        visited = {}

        root = self.nodes[0]
        queue.append(root)

        while len(queue) > 0:
            node = queue.pop(0)
            visited[node.value] = True
            visited_nodes_order.append(node.value)

            for child in node.children:
                if visited.get(child.value) is None:
                    queue.append(child)

        return visited_nodes_order

    def BFS_search(self, key):
        if len(self.nodes) == 0:
            return None

        queue = []
        visited = {}

        root = self.nodes[0]
        queue.append(root)

        while len(queue) > 0:
            node = queue.pop(0)
            if node.value == key:
                return node

            visited[node.value] = True
            for child in node.children:
                if visited.get(child.value) is None:
                    queue.append(child)

        return None
