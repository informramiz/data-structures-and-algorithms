from basicalgorithms.binarysearch.binary_search import binary_search_iterative
from basicalgorithms.binarysearch.binary_search import binary_search_recursive
from asserts.asserts import assert_


def test_binary_search(binary_search):
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 6
    expected_index = 6
    actual = binary_search(array, key)
    assert_(expected_index, actual)

    array = [0, 1]
    key = 1
    expected_index = 1
    actual = binary_search(array, key)
    assert_(expected_index, actual)


def tests():
    print("---> Testing iterative binary search")
    test_binary_search(binary_search_iterative)
    print("---> Testing recursive binary search")
    test_binary_search(binary_search_recursive)


tests()

