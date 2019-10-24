from lists.LinkedList import LinkedList

class Queue:
    def __init__(self):
        self._linked_list = LinkedList()
        self._queue_size = 0
        # always points to the position where next element will be added
        self._tail = None

    def size(self):
        return self._queue_size

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, data):
        self._linked_list.append(data)
        self._queue_size += 1
        if self._tail is None:
            self._tail = self._linked_list.head
        else:
            self._tail = self._tail.next

    def dequeue(self):
        if self.is_empty():
            self._tail = None
            return None

        front_value = self._linked_list.head.value
        self._linked_list.remove(front_value)
        self._queue_size -= 1
        return front_value
