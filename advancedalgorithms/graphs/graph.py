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

    def DFS_traversal_iterative(self):
        if len(self.nodes) == 0:
            return []

        stack = []
        visited_nodes_order = []
        is_visited = {}

        root = self.nodes[0]
        visited_nodes_order.append(root.value)
        is_visited[root] = True
        stack.append((root, 0))

        while len(stack) > 0:
            parent, next_child_index = stack.pop()

            if next_child_index >= len(parent.children):
                continue

            # push parent current state (for backtracking) so that we can check remaining children after flow
            # returns from checking next_child.children
            stack.append((parent, next_child_index + 1))

            next_child = parent.children[next_child_index]
            if is_visited.get(next_child) is not None:
                continue

            visited_nodes_order.append(next_child.value)
            is_visited[next_child] = True

            # add next_child to the stack so that we can check it's children
            stack.append((next_child, 0))

        return visited_nodes_order

    def DFS_traversal_recursive(self):
        if self.is_empty():
            return []

        return self.__DFS_traversal_recursive(self.nodes[0])

    def is_empty(self):
        return len(self.nodes) == 0

    def __DFS_traversal_recursive(self, node, is_visited={}):
        if not node:
            return []

        is_visited[node] = True
        visited_nodes_order = [node.value]

        for child in node.children:
            if is_visited.get(child) is None:
                visited_nodes_order += self.__DFS_traversal_recursive(child, is_visited)

        return visited_nodes_order

