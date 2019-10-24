from queues.queue_with_python_list import Queue


class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.value})"


class BST:
    def __init__(self):
        self.root = None

    def BFS(self):
        if self.root is None:
            return []

        # print using BFS
        queue = Queue()
        # (node, level) tuple
        queue.enqueue((self.root, 0))
        # list to maintain visit order
        visit_order = []
        # while there are still nodes to visit
        while not queue.is_empty():
            # visit the node at front of queue
            current_node, level = queue.dequeue()

            visit_order.append((current_node, level))

            # enqueue current node children to be discovered and visit candidate
            if current_node.left:
                queue.enqueue((current_node.left, level + 1))
            if current_node.right:
                queue.enqueue((current_node.right, level + 1))

        return visit_order

    def __repr__(self):
        visit_order = self.BFS()
        # print in the visit order
        string = "Tree"
        previous_level = -1
        for node, level in visit_order:
            if level == previous_level:
                string += " | " + str(node)
            else:
                string += "\n" + str(node)
            previous_level = level

        return string

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        node = self.root
        while node:
            if value == node.value:
                # ignore duplicates
                break
            elif value >= node.value:
                # go right
                if node.right:
                    node = node.right
                else:
                    # there is no right node so just insert new node here
                    node.right = Node(value)
                    break
            else:
                # go left
                if node.left:
                    node = node.left
                else:
                    # there is no left node so insert it here
                    node.left = Node(value)
                    break

    def is_empty(self):
        return self.root is None

    def search(self, value):
        return self.__search(value) is not None

    def __search(self, value):
        node = self.root
        while node:
            if value == node.value:
                return node

            if value >= node.value:
                # go right
                node = node.right
            else:
                # go left
                node = node.left

        return None

    def pre_order_traversal(self):
        return self._pre_order_traversal(self.root)

    def _pre_order_traversal(self, node):
        #parent first order
        output = [node.value]
        if node.left:
            output += self._pre_order_traversal(node.left)
        if node.right:
            output += self._pre_order_traversal(node.right)

        return output

    def in_order_traversal(self):
        return self._in_order_traversal(self.root)

    def _in_order_traversal(self, node):
        output = []
        if node.left:
            output += self._in_order_traversal(node.left)

        # parent in between
        output += [node.value]

        if node.right:
            output += self._in_order_traversal(node.right)

        return output

    def post_order_traversal(self):
        return self._post_order_traversal(self.root)

    def _post_order_traversal(self, node):
        output = []
        if node.left:
            output += self._post_order_traversal(node.left)

        if node.right:
            output += self._post_order_traversal(node.right)

        # parent after between
        output += [node.value]
        return output



