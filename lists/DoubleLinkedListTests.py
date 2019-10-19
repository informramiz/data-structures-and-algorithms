from DoublyLinkedList import *

def test_double_linked_list_append():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(-2)
    linked_list.append(4)

    assert(linked_list.to_list() == [1, -2, 4])
    assert(linked_list.to_list_reverse() == [4, -2, 1])
test_double_linked_list_append()
