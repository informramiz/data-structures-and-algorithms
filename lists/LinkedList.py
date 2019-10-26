class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, init_list = None, head = None):
        self.head = head
        if init_list:
            for value in init_list:
                self.append(value)

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
        """ Search the linked list for a node with the requested value and return the node. """
        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next
        return None

    def remove(self, value):
        """ Remove first occurrence of value. """
        if self.head.value == value:
            self.head = self.head.next
            return True

        node = self.head
        while node.next and node.next.value != value:
            node = node.next

        if node.next:
            node.next = node.next.next
            return True

        # Node not found
        return False

    def pop(self):
        """ Return the first node's value and remove it from the list. """
        if self.head:
            value = self.head.value
            self.head = self.head.next
            return value

        return None

    def insert(self, value, index):
        """ Insert value at pos position in the list. If pos is larger than the
            length of the list, append to the end of the list.
        """

        #take care of the head case first
        if index == 0:
            self.prepend(value)
            return
        elif self.head == None: #list empty
            self.head = Node(value)
            return

        current_index = 0
        node = self.head
        #stop when either list ends or right before the required position node
        while node.next and current_index < index-1:
            node = node.next
            current_index += 1

        if node.next:
            new_node = Node(value)
            new_node.next = node.next
            node.next = new_node
        else: #the required position is greater than current length
            node.next = Node(value)

    def size(self):
        """ Return the size or length of the linked list. """
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next

        return count

    def __iter__(self):
        #make class iterator protocol compliant to be used
        #as a Python container just like native lists so
        #you can write it like: [for node in linkedList] in loops
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        #this is called when print object directly for basic understanding of object
        return str([v for v in self])

    def reversed(self):
        """
        Reverse the inputted linked list

        Args:
           linked_list(obj): Linked List to be reversed
        Returns:
           obj: Reveresed Linked List
        """
        new_linked_list = LinkedList()
        for node in self:
            new_linked_list.prepend(node)

        return new_linked_list
