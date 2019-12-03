"""
Problem: A function that returns a boolean value indicating whether an element is present, but with no information about the location of that element.

For example:

letters = ['a', 'c', 'd', 'f', 'g']
print(contains('a', letters)) ## True
print(contains('b', letters)) ## False
"""

from basicalgorithms.binarysearch.binary_search import binary_search_iterative
from asserts.asserts import assert_


def contains(array, key):
    return binary_search_iterative(array, key) != -1


def tests():
    letters = ['a', 'c', 'd', 'f', 'g']
    output = contains(letters, 'a')
    assert_(expected=True, actual=output)

    output = contains(letters, 'b')
    assert_(expected=False, actual=output)


tests()

