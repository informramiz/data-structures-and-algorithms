"""
------------------Flattening a LinkedList--------------------
Suppose you have a linked list where the value of each node is a sorted linked
list (i.e., it is a nested list). Your task is to flatten this nested list—that
is, to combine all nested lists into a single (sorted) linked list.
"""

from LinkedList import LinkedList
from LinkedList import Node


# NestedLinkedList inherit LinkedList class, just for organization purposes
# otherwise NestedLinkedList and LinkedList are both exactly thing same
class NestedLinkedList(LinkedList):
    def flatten(self):
        """
        Idea is that each time we take 2 nodes' values (each node value is a LinkedList)
        and merge them. The nodes' values will be: first the already merged list
        which at start would be None as we are just starting, second the
        current node value (a LinkedList as each value is a LinkedList())
        """
        # at start the merged list is None because we are just starting
        merged = None
        # the take first node which at start is head
        node = self.head
        # keep going till you reach list end
        while node:
            # merged the current node value (which is a LinkedList) and
            # the already merged/Flattened LinkedList `merged`
            # Note: the merged method is defined below this class
            merged = merge(merged, node.value)
            # move to next node and repeat the merge process
            node = node.next
        # we have merged all nested linked lists by this point
        return merged


# first write a helper function to merge to 2 sorted lists
# As the lists are sorted so we have to merge them by taking
# their sort order into consideration
def merge(list1, list2):
    # if either of the lists is none then just return the
    # the other list
    if list1 is None:
        return list2
    elif list2 is None:
        return list1

    merged = LinkedList()
    l1_node = list1.head
    l2_node = list2.head

    # keep going until we have reached end of both lists
    while l1_node or l2_node:
        if l1_node is None:
            # we have reached end of list1 but not list2 otherwise loop would
            # have already ended so keep adding elements
            # of list2 until we reach its end
            merged.append(l2_node.value)
            # move to next node of the list2
            l2_node = l2_node.next
        elif l2_node is None:
            # we have reached end of list2 but not list1 otherwise loop would
            # have already ended so keep adding elements
            # of list1 until we reach its end
            merged.append(l1_node.value)
            # move to next node of the list1
            l1_node = l1_node.next
        # both lists are still going so add the list element with
        # smaller value because we have to keep the sort order when merging
        elif l1_node.value <= l2_node.value:
            # list1 current node value is smaller so add it to merged list
            merged.append(l1_node.value)
            # move to next node of the list1
            l1_node = l1_node.next
        else:
            # it means list2 current node value is smaller so add it to merged list
            merged.append(l2_node.value)
            # move to next node of the list2
            l2_node = l2_node.next

    # by this line we have reach end of both lists so both are merged
    return merged


# Test Cases
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


def test_flattening():
    linked_list = LinkedList(head=Node(1))
    linked_list.append(3)
    linked_list.append(5)

    second_linked_list = LinkedList(head=Node(2))
    second_linked_list.append(4)

    nested_linked_list = NestedLinkedList(head=Node(linked_list))
    nested_linked_list.append(second_linked_list)
    flattened = nested_linked_list.flatten()

    assert flattened.to_list() == [1, 2, 3, 4, 5], f"list contents: {flattened.to_list()}"


test_flattening()
