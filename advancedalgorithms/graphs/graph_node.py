"""
Author: Ramiz Raja
Created on: 22/01/2020
"""


class GraphNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, value):
        if isinstance(value, GraphNode):
            self.children.append(value)
        else:
            self.children.append(GraphNode(value))

    def remove_child(self, value):
        if isinstance(value, GraphNode):
            self._remove_child_node(value)
        else:
            self._remove_child(value)

    def _remove_child(self, value):
        node_to_remove = None
        for node in self.children:
            if node.value == value:
                node_to_remove = node

        if node_to_remove:
            self.children.remove(node_to_remove)

    def _remove_child_node(self, node):
        if node in self.children:
            self.children.remove(node)

    def __repr__(self):
        return f"Node({self.value}, {str([c.value for c in self.children])})"

