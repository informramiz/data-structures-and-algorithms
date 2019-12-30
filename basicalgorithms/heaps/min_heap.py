"""
Heaps:
A heap is a data structure with the following two main properties:

1. Complete Binary Tree (Like the name suggests we use a binary tree to create heaps. A complete binary tree is a
special type of binary tree in which all levels must be filled except for the last level. Moreover, in the last level,
the elements must be filled from left to right.)

2. Heap Order Property - Heaps come in two flavor
 2.1. Min Heap
 2.2. Max Heap

Min Heap - In the case of min heaps, for each node, the parent node must be smaller than both the child nodes.
It's okay even if one or both of the child nodes do not exists. However if they do exist, the value of the parent
node must be smaller. Also note that it does not matter if the left node is greater than the right node or vice versa.
The only important condition is that the root node must be smaller than both it's child nodes
Max Heap - For max heaps, this condition is exactly reversed. For each node, the value of the parent node must be
larger than both the child nodes.

Thus, for a data structure to be called a Heap, it must satisfy both of the above properties.

1. It must be a complete binary tree
2. It must satisfy the heap order property. If it's a min heap, it must satisfy the heap order property for min heaps.
If it's a max heap, it should satisfy the heap order property for max heaps.
"""


class MinHeap(object):
    def __init__(self, initial_size: int):
        self.capacity = initial_size
        # complete binary tree holder array
        self.array = [None for _ in range(initial_size)]
        # next index to insert item on
        self.next_index = 0

    @staticmethod
    def parent_to_left_child_index(parent_index):
        return (2 * parent_index) + 1

    @staticmethod
    def child_to_parent_index(child_index):
        return (child_index - 1) // 2

    def insert(self, data):
        self.array[self.next_index] = data
        parent_index = MinHeap.child_to_parent_index(self.next_index)
        self.__heapify_up(parent_index)
        self.next_index += 1
        if self.next_index == self.capacity:
            self.__handle_out_of_capacity()

    def __handle_out_of_capacity(self):
        # double the capacity
        self.capacity *= 2

        # copy old elements into new array
        temp = self.array
        self.array = [None for _ in range(self.capacity)]
        for index in range(self.next_index):
            self.array[index] = temp[index]

    def __heapify_up(self, parent_index):
        while parent_index > 0:
            child1_index = MinHeap.parent_to_left_child_index(parent_index)
            child2_index = child1_index + 1

            if self.array[parent_index] > self.array[child1_index]:
                #  parent is greater than left child, swap
                parent = self.array[parent_index]
                self.array[parent_index] = self.array[child1_index]
                self.array[child1_index] = parent
            elif self.array[parent_index] > self.array[child2_index]:
                #  parent is greater than right child, swap
                parent = self.array[parent_index]
                self.array[parent_index] = self.array[child2_index]
                self.array[child2_index] = parent
            else:
                # parent is good, heap order property is fine so no need to heapify any further
                break

            # verify the parent of current parent to check if heapify is needed
            parent_index = MinHeap.child_to_parent_index(parent_index)

    def peek(self):
        if self.is_empty():
            return None
        return self.array[self.next_index-1]

    def remove(self):
        """
        Remove and return the element at the top of the heap
        """

        if self.is_empty():
            return None

        # swap first and last elements
        last_element = self.array[self.next_index-1]
        self.array[self.next_index-1] = self.array[0]
        self.array[0] = last_element

        # now delete the last element
        self.next_index -= 1
        self.array[self.next_index] = None

        # now make sure heap order property is correct
        self.__down_heapify()

        return last_element

    def __down_heapify(self):
        parent_index = 0
        while parent_index is not None:
            left_child_index = MinHeap.parent_to_left_child_index(parent_index)
            right_child_index = left_child_index + 1

            parent = self.array[parent_index]
            if left_child_index >= self.capacity or self.array[left_child_index] is None:
                # the parent has no children so we are done with heapify
                break
            elif self.array[left_child_index] < parent:
                # left child is smaller than parent so swap
                self.array[parent_index] = self.array[left_child_index]
                self.array[left_child_index] = parent
                # now check the children of the left child
                parent_index = left_child_index
            elif right_child_index < self.capacity and self.array[right_child_index] is not None:
                # the right child is smaller than parent so swap
                if self.array[right_child_index] < parent:
                    self.array[parent_index] = self.array[right_child_index]
                    self.array[right_child_index] = parent
                    # now check the children of the right child
                    parent_index = left_child_index
                else:
                    # parent is smaller than both left and right children so heap order property is fine now, no
                    # need to heapify any further
                    break
            else:
                # there are no more children to check
                break

    def size(self):
        return self.next_index

    def is_empty(self):
        return self.size() == 0

    def to_list(self):
        return [v for v in self.array if v is not None]

    def __repr__(self):
        return str(self.to_list())