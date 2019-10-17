class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

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

    def prepend(self, value):
        """ Prepend a value to the beginning of the list."""
        if self.head == None:
            self.head = Node(value)
            return

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def search(self, value):
        node = self.head
        while node:
            if node.value == value:
                return node
        return node

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

def test_comprehensive():
    # Test prepend
    linked_list = LinkedList()
    linked_list.prepend(1)
    assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
    linked_list.append(3)
    linked_list.prepend(2)
    assert linked_list.to_list() == [2, 1, 3], f"list contents: {linked_list.to_list()}"

    # Test append
    linked_list = LinkedList()
    linked_list.append(1)
    assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
    linked_list.append(3)
    assert linked_list.to_list() == [1, 3], f"list contents: {linked_list.to_list()}"

    # Test search
    linked_list.prepend(2)
    linked_list.prepend(1)
    linked_list.append(4)
    linked_list.append(3)
    assert linked_list.search(1).value == 1, f"list contents: {linked_list.to_list()}"
    assert linked_list.search(4).value == 4, f"list contents: {linked_list.to_list()}"
test_comprehensive()
