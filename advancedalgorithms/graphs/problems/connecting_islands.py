"""
Author: Ramiz Raja
Created on: 24/01/2020
Problem: In an ocean, there are n islands some of which are connected via bridges. Travelling over a
bridge has some cost attaced with it. Find bridges in such a way that all islands are connected
with minimum cost of travelling.

You can assume that there is at least one possible way in which all islands are connected with each other.

You will be provided with two input parameters:

num_islands = number of islands

bridge_config = list of lists. Each inner list will have 3 elements:

 a. island A
 b. island B
 c. cost of bridge connecting both islands
Each island is represented using a number

Example:

num_islands = 4
bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
Input parameters explanation:

1. Number of islands = 4
2. Island 1 and 2 are connected via a bridge with cost = 1
   Island 2 and 3 are connected via a bridge with cost = 4
   Island 1 and 4 are connected via a bridge with cost = 3
   Island 4 and 3 are connected via a bridge with cost = 2
   Island 1 and 3 are connected via a bridge with cost = 10
In this example if we are connecting bridges like this...

between 1 and 2 with cost = 1
between 1 and 4 with cost = 3
between 4 and 3 with cost = 2
...then we connect all 4 islands with cost = 6 which is the minimum traveling cost.
"""
from asserts.asserts import assert_
from advancedalgorithms.graphs.dijkstrasalgorithm.dijkstra_algorithm import *
from queue import PriorityQueue


def build_graph(num_islands, bridge_config):
    adjacency_list = [list() for _ in range(num_islands+1)]
    for bridge in bridge_config:
        island_a, island_b, cost = bridge
        adjacency_list[island_a].append((island_b, cost))
        adjacency_list[island_b].append((island_a, cost))

    return adjacency_list


def get_minimum_cost_of_connecting(num_islands, bridge_config):
    """
    :param: num_islands - number of islands
    :param: bridge_config - bridge configuration as explained in the problem statement
    return: cost (int) minimum cost of connecting all islands
    """
    adjacency_list = build_graph(num_islands, bridge_config)
    start_vertex = 1
    is_visited = [False for _ in range(len(adjacency_list) + 1)]
    priority_queue = PriorityQueue()
    priority_queue.put_nowait((0, start_vertex))

    total_cost = 0
    while priority_queue.qsize() > 0:
        cost, selected_vertex = priority_queue.get_nowait()
        if is_visited[selected_vertex]:
            continue

        total_cost += cost
        is_visited[selected_vertex] = True

        # add neighbors
        for neighbor, edge_cost in adjacency_list[selected_vertex]:
            if not is_visited[neighbor]:
                priority_queue.put_nowait((edge_cost, neighbor))

    return total_cost


def test_function(test_case):
    num_islands = test_case[0]
    bridge_config = test_case[1]
    solution = test_case[2]
    output = get_minimum_cost_of_connecting(num_islands, bridge_config)
    assert_(expected=solution, actual=output)


def tests():
    num_islands = 4
    bridge_config = [[1, 2, 1], [2, 3, 4], [1, 4, 3], [4, 3, 2], [1, 3, 10]]
    solution = 6
    test_case = [num_islands, bridge_config, solution]
    test_function(test_case)

    num_islands = 5
    bridge_config = [[1, 2, 5], [1, 3, 8], [2, 3, 9]]
    solution = 13
    test_case = [num_islands, bridge_config, solution]
    test_function(test_case)

    num_islands = 5
    bridge_config = [[1, 2, 3], [1, 5, 9], [2, 3, 10], [4, 3, 9]]
    solution = 31
    test_case = [num_islands, bridge_config, solution]
    test_function(test_case)


tests()


