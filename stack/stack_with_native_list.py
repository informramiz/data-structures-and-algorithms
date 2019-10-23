"""
Before we start let us reiterate they key components of a stack. A stack is a data structure that consists of two
main operations: push and pop. A push is when you add an element to the top of the stack and a pop is when
you remove an element from the top of the stack. Python 3.x conviently allows us to demonstrate this
functionality with a list. When you have a list such as [2,4,5,6] you can decide which end of the list is the bottom
and the top of the stack respectivley. Once you decide that, you can use the append, pop or insert function to
simulate a stack. We will choose the first element to be the bottom of our stack and therefore be using the
append and pop functions to simulate it. Give it a try by implementing the function below!
"""

class Stack:
    def __init__(self):
        self._list = []

    def push(self, value):
        self._list.append(value)

    def __repr__(self):
        return str(self._list)

    def size(self):
        return len(self._list)

    def pop(self):
        if self.is_empty():
            return None

        return self._list.pop()

    def top(self):
        if self.is_empty():
            return None

        return self._list[-1]

    def is_empty(self):
        return self.size() == 0
