from basicalgorithms.heaps.min_heap import *
from asserts.asserts import assert_


def tests():
    min_heap = MinHeap(10)
    min_heap.insert(1)
    min_heap.insert(3)
    min_heap.insert(2)
    assert_(expected=[1, 3, 2], actual=min_heap.to_list())


tests()
