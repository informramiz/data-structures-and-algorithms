class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head == None:
            self.head = DoubleNode(value)
            self.tail = self.head
            return

        new_node = DoubleNode(value)
        new_node.previous = self.tail
        self.tail.next = new_node
        self.tail = self.tail.next

def test_double_linked_list_append():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(-2)
    linked_list.append(4)

    forward_list = []
    node = linked_list.head
    while node:
        forward_list.append(node.value)
        node = node.next
    assert(forward_list == [1, -2, 4])

    backward_list = []
    node = linked_list.tail
    while node:
        backward_list.append(node.value)
        node = node.previous
    assert(backward_list == [4, -2, 1])
test_double_linked_list_append()
