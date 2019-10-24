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
                queue.enqueue((current_node, level + 1))

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
