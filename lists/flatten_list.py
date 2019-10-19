"""
------------------Flattening a LinkedList--------------------
Suppose you have a linked list where the value of each node is a sorted linked
list (i.e., it is a nested list). Your task is to flatten this nested list—that
is, to combine all nested lists into a single (sorted) linked list.
"""

from LinkedList import LinkedList
from LinkedList import Node


# first write a helper function to merge to 2 sorted lists
def merge(list1, list2):
    if list1 is None:
        return list2
    elif list2 is None:
        return list1

    merged = LinkedList()
    l1_node = list1.head
    l2_node = list2.head
    while l1_node or l2_node:
        if l1_node is None:
            merged.append(l2_node.value)
            l2_node = l2_node.next
        elif l2_node is None:
            merged.append(l1_node.value)
            l1_node = l1_node.next
        elif l1_node.value <= l2_node.value:
            merged.append(l1_node.value)
            l1_node = l1_node.next
        else:
            merged.append(l2_node.value)
            l2_node = l2_node.next

    return merged


def test_merge():
    linked_list = LinkedList(head=Node(1))
    linked_list.append(3)
    linked_list.append(5)

    second_linked_list = LinkedList(head=Node(2))
    second_linked_list.append(4)

    merged = merge(linked_list, second_linked_list)
    assert merged.to_list() == [1, 2, 3, 4, 5], f"List contents: {merged.to_list()}"

    # Lets make sure it works with a None list
    merged = merge(None, linked_list)
    assert merged.to_list() == [1, 3, 5], f"List contents: {merged.to_list()}"



test_merge()
