"""
Problem Statement
You are given the head of a linked list and two integers, i and j. You have to retain the first i nodes and then delete
the next j nodes. Continue doing so until the end of the linked list.

Example:

linked-list = 1 2 3 4 5 6 7 8 9 10 11 12
i = 2
j = 3
Output = 1 2 6 7 11 12
"""

from lists.LinkedList import LinkedList
from lists.LinkedList import Node


def skip_i_delete_j(head: Node, i, j):
    if head is None or j <= 0:
        return head
    elif i <= 0:
        return None

    current_node = head
    while current_node:
        # skip (i-1) nodes, (i-1) because current_node is already pointing to a proper node so 1 node is already skipped
        for _ in range(i-1):
            if current_node is None:
                return head
            current_node = current_node.next

        previous_node = current_node
        # skip the next j nodes
        current_node = current_node.next
        for _ in range(j):
            if current_node is None:
                # make sure list is ending with the last node pointing to None
                previous_node.next = None
                return head
            current_node = current_node.next

        # connect previous i-node with (j+1)th node after skipping j nodes
        previous_node.next = current_node

    return head


def test_case(inputt, i, j, expected_output):
    linked_list = LinkedList()
    for value in inputt:
        linked_list.append(value)

    actual_output = skip_i_delete_j(linked_list.head, i, j)
    output_list = LinkedList(head=actual_output).to_list()
    assert expected_output == output_list, f"expected={expected_output}, actual={output_list}"


def test():
    # Test-1
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    i = 2
    j = 2
    solution = [1, 2, 5, 6, 9, 10]
    test_case(arr, i, j, solution)

    # Test-2
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    i = 2
    j = 3
    solution = [1, 2, 6, 7, 11, 12]
    test_case(arr, i, j, solution)

    # Test-3
    arr = [1, 2, 3, 4, 5]
    i = 2
    j = 4
    solution = [1, 2]
    test_case(arr, i, j, solution)

    arr = [1, 2, 3, 4, 5]
    i = 0
    j = 4
    solution = []
    test_case(arr, i, j, solution)

    
test()
