from lists.LinkedList import LinkedList


class Stack:
    def __init__(self, initial_size = 10):
        self._linked_list = LinkedList()
        # always point to the position where the next element will be inserted
        self._top = 0

    def push(self, value):
        self._linked_list.prepend(value)
        self._top += 1

    def __repr__(self):
        return str(self._linked_list.to_list())

    def size(self):
        return self._top

    def pop(self):
        if self.is_empty():
            return None

        self._top -= 1
        top_value = self.top()
        self._linked_list.remove(top_value)
        return top_value

    def top(self):
        if self.is_empty():
            return None
        return self._linked_list.head.value

    def is_empty(self):
        return self._top == 0