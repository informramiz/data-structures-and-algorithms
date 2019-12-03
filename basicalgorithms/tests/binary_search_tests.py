from basicalgorithms.binary_search import binary_search_iterative
from asserts.asserts import assert_


def test_binary_search():
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    key = 6
    expected_index = 6
    actual = binary_search_iterative(array, key)
    assert_(expected_index, actual)

    array = [0, 1]
    key = 1
    expected_index = 1
    actual = binary_search_iterative(array, key)
    assert_(expected_index, actual)


test_binary_search()
