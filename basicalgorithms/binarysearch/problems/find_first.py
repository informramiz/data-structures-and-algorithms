"""
Problem: Find First
The binary search function is guaranteed to return an index for the element you're looking for in an array,
but what if the element appears more than once? In this case you should return the first occurring element index

Consider this array:

[1, 3, 5, 7, 7, 7, 8, 11, 12]

Let's find the number 7: should return index 3
if a number is not found the return None
"""

from basicalgorithms.binarysearch.binary_search import binary_search_iterative
from asserts.asserts import assert_


def find_first(array, key):
    key_index = binary_search_iterative(array, key)
    if key_index == -1:
        return None

    #  we need to find the first occurrence in case of duplication, if there will be any duplication and if
    #  the found index is not the first occurrence then first occurrence will be in range [0, key_index-1]
    while key_index > 0 and array[key_index-1] == key:
        key_index -= 1

    return key_index


def tests():
    array = [1, 3, 5, 7, 7, 7, 8, 11, 12]
    key = 7
    assert_(expected=3, actual=find_first(array, key))

    array = [1, 3, 3, 3]
    key = 3
    assert_(expected=1, actual=find_first(array, key))

    array = [1, 3, 3, 3]
    key = 9
    assert_(expected=None, actual=find_first(array, key))


tests()
