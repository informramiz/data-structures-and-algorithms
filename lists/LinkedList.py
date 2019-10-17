from Node import *

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            return

        tail = self.head
        while tail.next:
            tail = tail.next

        tail.next = Node(value)

    def to_list(self):
        #Write function to turn Linked List into Python List
        list = []
        tail = self.head
        while tail:
            list.append(tail.value)
            tail = tail.next

        return list

def test_linked_list_basic():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(4)

    node = linked_list.head
    while node:
        print(node.value)
        node = node.next
test_linked_list_basic()

def test_linked_list_to_python_list():
    linked_list = LinkedList()
    linked_list.append(3)
    linked_list.append(2)
    linked_list.append(-1)
    linked_list.append(0.2)

    print ("Pass" if  (linked_list.to_list() == [3, 2, -1, 0.2]) else "Fail")
test_linked_list_to_python_list()
