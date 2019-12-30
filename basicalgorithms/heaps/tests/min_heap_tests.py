from basicalgorithms.heaps.min_heap import *
from asserts.asserts import assert_


def tests():
    min_heap = MinHeap(2)
    min_heap.insert(1)
    min_heap.insert(3)
    min_heap.insert(2)
    assert_(expected=4, actual=min_heap.capacity)
    assert_(expected=[1, 3, 2], actual=min_heap.to_list())

    min_heap.remove()
    assert_(expected=[2, 3], actual=min_heap.to_list())


tests()
