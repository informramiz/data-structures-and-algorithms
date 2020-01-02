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
                    return current_node.left

    def __rebalance(self, node):
        # case-1: if inserted node is root node, do nothing
        if node.parent is None:
            return
        parent = node.parent
        if parent.color is Color.BLACK:
            # case-2: black parent
            # no rule broken, do nothing
            return

        # case-3: inserted node (which is always red) has a red parent, rule-3 (red parent must have black children)
        # is broken
        # solution: If parent and it's sibling are both red, change them both to black and change grandparent to red
        pibling = RedBlackTree.__pibling(node)
        grandparent = RedBlackTree.__grand_parent(node)
        if pibling and pibling.color is Color.RED:
            node.parent.color = Color.BLACK
            pibling.color = Color.BLACK
            grandparent.color = Color.RED
            # make sure grandparent after color change does not break any rules otherwise re-balance it
            self.__rebalance(grandparent)
            return

        # it is either CASE-4 and CASE-5 or just CASE-5

        if grandparent is None:
            # case-4 and case-5 are only applicable when there is a grandparent otherwise they are not applicable
            return

        # case-4: inserted node's parent is red but it's sibling is not red and inserted node and it's parent
        # are not on the same side
        # check if Left-Right or Right-Left case
        if RedBlackTree.__is_case4(node, grandparent):
            if node == parent.right:
                # Left-Right case so rotate left on parent
                RedBlackTree.__rotate_left_on_parent(node)
            else:
                # Right-Left case so rotate right on parent
                RedBlackTree.__rotate_right_on_parent(node)

            # after any of above rotations, node and parent roles are swapped so reflect the same in code
            temp = parent
            parent = node
            node = temp

        # After applying case-4 it will be automatically eligible for case-5 so apply CASE-5 as well
        # CASE-5: When node and it's parent are on same side of the grandparent (LL or RR case)
        # then we apply left/right rotation
        # on grandparent instead of parent
        if parent.right == node:
            # Right-Right case so rotate left on grandparent
            RedBlackTree.__rotate_left_on_grandparent(node)
        else:
            # Left-Left case so rotate right on grandparent
            RedBlackTree.__rotate_right_on_grandparent(node)

    @staticmethod
    def __grand_parent(node):
        if node.parent is None:
            return None
        return node.parent.parent

    @staticmethod
    def __pibling(node):
        # a parent's sibling is calling pibling
        p = node.parent
        if p is None:
            return None

        gp = RedBlackTree.__grand_parent(node)
        if gp is None:
            return None
        if p == gp.left:
            return gp.right
        else:
            return gp.left

    @staticmethod
    def __is_case4(node, grandparent):
        """
        check if Left-Right or Right-Left case
        :param node:
        :param grandparent:
        :return:
        """
        parent = node.parent
        if parent == grandparent.left and node == parent.right:
            # Left-Right case so Rotate Left on parent case
            return True
        elif parent == grandparent.right and node == parent.left:
            # Right-Left case so Rotate Right on parent case
            return True

        return False

    @staticmethod
    def __rotate_left_on_parent(node):
        parent = node.parent
        gp = parent.parent

        # make parent left child of node
        parent.parent = node
        parent.right = node.left

        # make node parent and son of grand parent
        node.parent = gp
        node.left = parent

    @staticmethod
    def __rotate_right_on_parent(node):
        parent = node.parent
        gp = parent.parent

        # make parent right child of node
        parent.parent = node
        parent.left = node.right

        # make node son of grand parent and
        node.parent = gp
        node.right = parent

    @staticmethod
    def __rotate_left_on_grandparent(node):
        parent = node.parent
        gp = parent.parent
        ggp = gp.parent

        # make grandparent left child of parent
        gp.parent = parent
        gp.right = parent.left

        # make parent son of grand-grandparent
        parent.parent = ggp
        parent.left = gp

        # swap colors of parent and gp
        parent.color = Color.BLACK
        gp.color = Color.RED

        if ggp:
            if ggp.left == gp:
                ggp.left = parent
            else:
                ggp.right = parent

    @staticmethod
    def __rotate_right_on_grandparent(node):
        parent = node.parent
        gp = parent.parent
        ggp = gp.parent

        # make grandparent left child of parent
        gp.parent = parent
        gp.left = parent.right

        # make parent son of grand-grandparent
        parent.parent = ggp
        parent.right = gp

        # swap colors of parent and gp
        parent.color = Color.BLACK
        gp.color = Color.RED

        if ggp:
            if ggp.left == gp:
                ggp.left = parent
            else:
                ggp.right = parent

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
        string = ""
        for node, level in visited_nodes:
            string += '   ' * (level - 1) + '+--' * (level > 0) + '%s' % node + "\n"

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
        if self.is_empty():
            return False

        node = self.root
        while node:
            if node.value == value:
                return True
            elif value > node.value:
                node = node.right
            else:
                node = node.left

        return False
