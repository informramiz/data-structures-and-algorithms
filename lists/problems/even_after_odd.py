"""
Problem Statement
Given a linked list with integer data, arrange the elements in such a manner that all nodes with even numbers are placed
after odd numbers. Do not create any new nodes and avoid using any other data structure. The relative order of even and
odd elements must not change.

Example:

linked list = 1 2 3 4 5 6
output = 1 3 5 2 4 6
"""

from lists.LinkedList import LinkedList
from lists.LinkedList import Node


def even_after_odd(head: Node):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    if head is None or head.next is None:
        return head

    node = head
    even_head = None
    even_tail = None
    odd_head = None
    odd_tail = None
    while node:
        if node.value % 2 == 0:
            if even_head is None:
                even_head = node
                even_tail = node
            else:
                even_tail.next = node
                even_tail = even_tail.next
        else:  # odd
            if odd_head is None:
                odd_head = node
                odd_tail = node
            else:
                odd_tail.next = node
                odd_tail = odd_tail.next

        node = node.next

    # make sure last element of even list point to None as it will be the end of whole list
    if even_tail is not None:
        even_tail.next = None

    if odd_head is None:
        return even_head

    # assign even list to end of odd list
    odd_tail.next = even_head
    return odd_head


def test_case(input, expected_output):
    list1 = LinkedList()
    for value in input:
        list1.append(value)

    actual_output = LinkedList(head = even_after_odd(list1.head)).to_list()
    assert expected_output == actual_output, f"expected={expected_output}, actual={actual_output}"


def test():
    test_case([1, 2, 3, 4, 5, 6], [1, 3, 5, 2, 4, 6])
    test_case([1, 3, 5, 7], [1, 3, 5, 7])
    test_case([2, 4, 6, 8], [2, 4, 6, 8])


test()

