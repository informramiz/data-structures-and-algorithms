"""
Author: Ramiz Raja
Created on: 03/01/2020

Problem: Counting Inversionsd
The number of inversions in a disordered list is the number of pairs of elements that are inverted (out of order) in the list.

Here are some examples:

[0,1] has 0 inversions
[2,1] has 1 inversion (2,1)
[3, 1, 2, 4] has 2 inversions (3, 2), (3, 1)
[7, 5, 3, 1] has 6 inversions (7, 5), (3, 1), (5, 1), (7, 1), (5, 3), (7, 3)
The number of inversions can also be thought of in the following manner.

Given an array arr[0 ... n-1] of n distinct positive integers, for indices i and j, if i < j and arr[i] > arr[j]
then the pair (i, j) is called an inversion of arr.
"""

from asserts.asserts import assert_


def count_inversions(array):
    return _merge_sort(array, 0, len(array)-1)


def _merge_sort(array, start, end):
    if (end-start+1) <= 1:
        return 0

    m = (start + end) // 2
    inversions = _merge_sort(array, start, m)
    inversions += _merge_sort(array, m+1, end)
    inversions += merge_sorted_arrays(array, start, m, m+1, end)
    return inversions


def merge_sorted_arrays(array, start1, end1, start2, end2):
    size1 = end1 - start1 + 1
    size = end2 - start1 + 1
    sorted_array = [0] * size

    index1 = start1
    index2 = start2
    inversions = 0
    for i in range(size):
        if index1 > end1:
            sorted_array[i] = array[index2]
            index2 += 1
        elif index2 > end2:
            sorted_array[i] = array[index1]
            index1 += 1
        elif array[index1] <= array[index2]:
            sorted_array[i] = array[index1]
            index1 += 1
        else:
            sorted_array[i] = array[index2]
            index2 += 1
            inversions += size1 - (index1 - start1)

    for i in range(size):
        array[start1 + i] = sorted_array[i]

    return inversions


def tests():
    array = [2, 1]
    inversions = count_inversions(array)
    assert_(expected=1, actual=inversions)

    array = [3, 1, 2, 4]
    inversions = count_inversions(array)
    assert_(expected=2, actual=inversions)

    array = [7, 5, 3, 1]
    inversions = count_inversions(array)
    assert_(expected=6, actual=inversions)

    array = [2, 5, 1, 3, 4]
    inversions = count_inversions(array)
    assert_(expected=4, actual=inversions)

    array = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
    inversions = count_inversions(array)
    assert_(expected=26, actual=inversions)

    array = [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
    inversions = count_inversions(array)
    assert_(expected=2, actual=inversions)


tests()
