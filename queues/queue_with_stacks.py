from stack.stack_with_native_list import Stack

class Queue:
    def __init__(self):
        self._in_storage_stack = Stack()
        self._out_storage_stack = Stack()

    def size(self):
        return self._in_storage_stack.size() + self._out_storage_stack.size()

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, data):
        self._in_storage_stack.push(data)

    def dequeue(self):
        if self._out_storage_stack.top() is None:
            # move elements from in_storage_stack to out storage stack. Notice as you move elements from in to out
            # storage stack their order in out_storage_stack becomes the desired order in a queue
            while self._in_storage_stack.top() is not None:
                self._out_storage_stack.push(self._in_storage_stack.pop())

        return self._out_storage_stack.pop()
