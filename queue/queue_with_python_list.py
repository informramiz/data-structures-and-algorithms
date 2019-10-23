class Queue:
    def __init__(self):
        self._items = []

    def size(self):
        return len(self._items)

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, data):
        self._items.append(data)

    def dequeue(self):
        return self._items.pop(0)
