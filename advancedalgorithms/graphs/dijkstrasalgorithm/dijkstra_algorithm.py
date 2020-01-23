"""
Author: Ramiz Raja
Created on: 23/01/2020
"""
from queue import PriorityQueue
import math


class Edge(object):
    def __init__(self, node, distance):
        self.node = node
        self.distance = distance

    def __repr__(self):
        return f"({self.node}, {self.distance})"


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

    def __repr__(self):
        return str(self.value)


class Graph(object):
    def __init__(self, nodes_list=None):
        if nodes_list is None:
            nodes_list = []
        self.nodes = nodes_list

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.nodes)

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


class DijkstraNode(object):
    def __init__(self, node, weight):
        self.node = node
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __iter__(self):
        yield self.node
        yield self.weight

    def __repr__(self):
        return f"({self.node}, {self.weight})"


def dijkstra(start_node, end_node):
    if start_node == end_node:
        return [start_node, end_node]

    min_queue = PriorityQueue()
    min_queue.put_nowait(DijkstraNode(start_node, 0))

    # other variables to run Dijkstra algo
    nodes_selection_order = []
    is_selected = {}
    weights = {start_node: 0}

    # dictionary to keep track of which parent was the latest to update which node, this will help in
    # extracting path information at the end
    parent = {}

    # set the weight of start node as 0
    while not min_queue.empty():
        # get the next min node and it's weight
        selected_node, selected_node_weight = min_queue.get_nowait()

        if is_selected.get(selected_node):
            # this is to avoid duplication because I am not removing nodes from min_queue when updating
            # their weights (I just add a new DijkstraNode with new weight) so there will be duplicates
            # but overall distance calculation will not be affected
            continue

        # we have exhausted all the reachable nodes but did not find the destination node
        # that means there is no path from start_node to end_node
        if selected_node_weight == math.inf:
            return None

        # mark this node as selected into the path and add it to path
        is_selected[selected_node] = True
        nodes_selection_order.append(selected_node.value)

        if selected_node == end_node:
            # we have found the destination_node so path is found so return it
            path = build_path(parent, start_node, end_node)
            return path, selected_node_weight

        # go through all the adjacent edges/nodes from selected_node and update their weights if needed
        update_adjacent_nodes_weights(is_selected, min_queue, parent, selected_node, selected_node_weight, weights)

    return None


def update_adjacent_nodes_weights(is_selected, min_queue, parent, selected_node, selected_node_weight, weights):
    # go through all the adjacent edges/nodes from selected_node and update their weights if needed
    for edge in selected_node.edges:
        if is_selected.get(edge.node):
            # selected nodes are already part of path and can't be visited now
            continue

        new_weight = selected_node_weight + edge.distance
        if weights.get(edge.node, math.inf) == math.inf:
            # edge.node has not been visited yet so set it's weight
            weights[edge.node] = new_weight
            parent[edge.node] = selected_node
            min_queue.put_nowait(DijkstraNode(edge.node, new_weight))
        else:
            # edge.node has been visited before so check if it's weight can minimized by taking path
            # from selected_node
            prev_weight = weights[edge.node]
            if prev_weight > new_weight:
                weights[edge.node] = new_weight
                parent[edge.node] = selected_node
                min_queue.put_nowait(DijkstraNode(edge.node, new_weight))


def build_path(parent, start_node, end_node):
    path = [end_node.value]
    current_parent = parent[end_node]
    while current_parent != start_node:
        path.append(current_parent.value)
        current_parent = parent[current_parent]

    path.append(start_node.value)
    path.reverse()
    return path
