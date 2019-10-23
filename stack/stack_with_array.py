"""
Our goal will be to implement a Stack class that has the following behaviors:

push - adds an item to the top of the stack
pop - removes an item from the top of the stack (and returns the value of that item)
size - returns the size of the stack
top - returns the value of the item at the top of stack (without removing that item)
is_empty - returns True if the stack is empty and False otherwise
"""


class Stack:
    def __init__(self, initial_size = 10):
        self._array = [None for _ in range(initial_size)]
        # always point to the position where the next element will be inserted
        self._top = 0

    def _handle_stack_capacity_full(self):
        old_array = self._array
        # create a new array of double the original size
        new_array = [None for _ in range(2*len(old_array))]
        # copy the elements from old to new array
        for i in range(len(old_array)):
            new_array[i] = old_array[i]

        self._array = new_array

    def push(self, value):
        if self._top == len(self._array):
            self._handle_stack_capacity_full()

        self._array[self._top] = value
        self._top += 1

    def __repr__(self):
        return str([v for v in self._array])

    def size(self):
        return self._top

    def capacity(self):
        return len(self._array)

    def pop(self):
        if self.is_empty():
            return None

        self._top -= 1
        top_value = self._array[self._top]
        return top_value

    def top(self):
        if self.is_empty():
            return None

        return self._array[self._top - 1]

    def is_empty(self):
        return self._top == 0
