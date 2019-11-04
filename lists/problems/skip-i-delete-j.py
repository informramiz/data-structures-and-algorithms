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

    current_node = head
    new_head = None
    new_tail = None
    count = 0
    is_skip_done = False
    while current_node:
        if not is_skip_done and count >= i:
            # i nodes are skipped, reset counter and mark is_skip_done as True
            is_skip_done = True
            count = 0
        elif is_skip_done and count >= j:
            # j nodes are ignored/deleted so reset counter and skip flag
            count = 0
            is_skip_done = False

        if not is_skip_done and count < i:
            # if i not node are not skipped yet, then keep them as part of new_head
            if new_tail:
                new_tail.next = current_node
                new_tail = new_tail.next
            else:
                new_head = current_node
                new_tail = current_node

        current_node = current_node.next
        count += 1

    # it is possible that the end of new_head, new_tail is not None so set it to None
    if new_tail:
        new_tail.next = None

    return new_head


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


test()
