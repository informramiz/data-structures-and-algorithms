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

    def to_list(self):
        #Write a function to convert DoublyLinkedList to Python list
        list = []
        node = self.head
        while node:
            list.append(node.value)
            node = node.next

        return list

    def to_list_reverse(self):
        list = []
        node = self.tail
        while node:
            list.append(node.value)
            node = node.previous

        return list
