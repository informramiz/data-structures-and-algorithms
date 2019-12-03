"""
Problem statement:
Given a sorted array that may have duplicate values, use binary search to find the first and last indexes of a given value.

For example, if you have the array [0, 1, 2, 2, 3, 3, 3, 4, 5, 6] and the given value is 3, the answer will be [4, 6]
(because the value 3 occurs first at index 4 and last at index 6 in the array).

The expected complexity of the problem is  𝑂(𝑙𝑜𝑔(𝑛)) .
"""

from basicalgorithms.binarysearch.binary_search import binary_search_iterative
from asserts.asserts import assert_


# solution1
def first_and_last_index_iterative(array, key):
    key_index = binary_search_iterative(array, key)
    if key_index == -1:
        return [-1, -1]

    #  we need to find the first occurrence in case of duplication, if there will be any duplication and if
    #  the found index is not the first occurrence then first occurrence will be in range [0, key_index-1]
    start_index = key_index
    while start_index > 0 and array[start_index-1] == key:
        start_index -= 1

    #  we need to find the last occurrence in case of duplication, if there will be any duplication and if
    #  the found index is not the last occurrence then last occurrence will be in range [key_index, n-1]
    end_index = key_index
    n = len(array)
    while end_index < n-1 and array[end_index+1] == key:
        end_index += 1

    return [start_index, end_index]


# solution-2: It achieves the output in desired time
def find_first_and_last_index_recursive(array, key):
    first_index = find_first_index(array, key, 0, len(array) - 1)
    last_index = find_last_index(array, key, 0, len(array) - 1)
    return [first_index, last_index]


def find_first_index(array, key, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if array[mid] == key:
        # we need to find for first occurrence so let's check in range [start, mid-1]
        first_occurrence = find_first_index(array, key, start, mid-1)
        if first_occurrence == -1:
            # we did not find any other occurrence so mid is the first index then
            first_occurrence = mid
        return first_occurrence
    elif key < array[mid]:
        #  key is in range [start, mid-1]
        return find_first_index(array, key, start, mid-1)
    else:
        # key is in range [mid+1, end]
        return find_first_index(array, key, mid+1, end)


def find_last_index(array, key, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if array[mid] == key:
        # we need to find for last occurrence so let's check in range [mid+1, end]
        last_index = find_last_index(array, key, mid+1, end)
        if last_index == -1:
            # we did not find any other occurrence so mid is the last index then
            last_index = mid
        return last_index
    elif key < array[mid]:
        #  key is in range [start, mid-1]
        return find_last_index(array, key, start, mid-1)
    else:
        # key is in range [mid+1, end]
        return find_last_index(array, key, mid+1, end)


def tests(first_and_last_index):
    array = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
    key = 3
    assert_(expected=[3, 6], actual=first_and_last_index(array, key))

    array = [1]
    key = 1
    assert_(expected=[0, 0], actual=first_and_last_index(array, key))

    array = [0, 1, 2, 3, 4, 5]
    key = 5
    assert_(expected=[5, 5], actual=first_and_last_index(array, key))

    key = 6
    assert_(expected=[-1, -1], actual=first_and_last_index(array, key))


def test():
    print("----> Testing iterative solution")
    tests(first_and_last_index_iterative)
    print("----> Testing recursive solution")
    tests(find_first_and_last_index_recursive)


test()
