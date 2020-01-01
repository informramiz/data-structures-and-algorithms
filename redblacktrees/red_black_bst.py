"""
Problem: Build a Red-Black Tree

Remember, we need to follow the red-black tree rules, on top of the binary search tree rules. Our new rules are:

- All nodes have a color
- All nodes have two children (use NULL nodes for missing children)
- All NULL nodes are colored black
- If a node is red, its children must be black
- The root node must be black (optional), we'll go ahead and implement without this for now
- Every path to its descendant NULL nodes must contain the same number of black nodes
"""


from redblacktrees.Node import *
from collections import deque


class RedBlackTree(object):
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def insert(self, value):
        if self.is_empty():
            self.root = Node(value, None, Color.RED)
            return

        inserted_node = self.__insert_helper(value)
        self.__rebalance(inserted_node)

    def __insert_helper(self, value) -> Node:
        current_node = self.root
        while current_node:
            if value == current_node.value:
                # ignore duplicates
                return current_node
            elif value > current_node.value:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    current_node.right = Node(value, current_node)
                    return current_node.right
            else:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    current_node.left = Node(value, current_node)
                    return current_node

    def __rebalance(self, node):
        pass

    def BFS(self):
        if self.is_empty():
            return []

        queue = deque()
        queue.append((self.root, 0))

        visited_nodes = []
        while len(queue) > 0:
            (node, level) = queue.popleft()
            visited_nodes.append((node, level))

            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))

        return visited_nodes

    def __repr__(self):
        visited_nodes = self.BFS()
        previous_level = -1
        string = ""
        for node, level in visited_nodes:
            if level == previous_level:
                string += " | " + str(node)
            else:
                string += "\n" + str(node)
            previous_level = level

        return string

    def in_order_traversal(self):
        return self.__in_order_traversal(self.root)

    def __in_order_traversal(self, node):
        if node is None:
            return []

        output = []
        if node.left is not None:
            output += self.__in_order_traversal(node.left)
        output += [node.value]
        if node.right is not None:
            output += self.__in_order_traversal(node.right)

        return output

    def search(self, value):
        pass
