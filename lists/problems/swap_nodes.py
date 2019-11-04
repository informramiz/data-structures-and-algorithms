"""
Problem Statement
Given a linked list, swap the two nodes present at position i and j. The positions are based on 0-based indexing.

Note: You have to swap the nodes and not just the values.

Example:

linked_list = 3 4 5 2 6 1 9
positions = 3 4
output = 3 4 5 6 2 1 9
Explanation:

The node at position 3 has the value 2
The node at position 4 has the value 6
Swapping these nodes will result in a final order of nodes of 3 4 5 6 2 1 9
"""

from lists.LinkedList import LinkedList
from lists.LinkedList import Node


def swap_nodes(head, i, j):
    """
    :param: head- head of input linked list
    :param: i - indicates position
    :param: j - indicates position
    return: head of updated linked list with nodes swapped
    swap nodes present at left_index and right_index and
    DO NOT create a new linked list
    """
    if head is None or i == j:
        return head

    i_node = None
    i_prev_node = None
    j_node = None
    j_prev_node = None

    index = 0
    current = head
    previous = None
    while current:
        if index == i:
            i_node = current
            i_prev_node = previous
        elif index == j:
            j_node = current
            j_prev_node = previous
            break

        previous = current
        current = current.next
        index += 1

    # if either i >= len(list) or j >= len(list), return as it is
    if i_node is None or j_node is None:
        return head

    # swap next nodes of i_node and j_node
    j_prev_node.next = i_node
    i_next_node = i_node.next
    i_node.next = j_node.next
    j_node.next = i_next_node

    # if the i node is head then update head to point to j_node
    if i_prev_node is None:
        head = j_node
    else:
        i_prev_node.next = j_node

    return head


def test_case(inputt, i, j, expected_output):
    linked_list = LinkedList()
    for value in inputt:
        linked_list.append(value)

    actual_output = swap_nodes(linked_list.head, i, j)
    output_list = LinkedList(head=actual_output).to_list()
    assert expected_output == output_list, f"expected={expected_output}, actual={output_list}"


def test():
    # Test-1
    arr = [3, 4, 5, 2, 6, 1, 9]
    i = 3
    j = 4
    solution = [3, 4, 5, 6, 2, 1, 9]
    test_case(arr, i, j, solution)

    # Test-2
    arr = [3, 4, 5, 2, 6, 1, 9]
    i = 2
    j = 5
    solution = [3, 4, 1, 2, 6, 5, 9]
    test_case(arr, i, j, solution)

    # Test-3
    arr = [3, 4, 5, 2, 6, 1, 9]
    i = 0
    j = 1
    solution = [4, 3, 5, 2, 6, 1, 9]
    test_case(arr, i, j, solution)

test()