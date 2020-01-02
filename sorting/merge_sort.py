"""
Author: Ramiz Raja
Created on: 02/01/2020

Problem: MergeSort
MergeSort is a divide and conquer algorithm that divides a list into equal halves until it has two single elements and
then merges the sub-lists until the entire list has been reassembled in order.

Divide
Our MergeSort code will focus first on the divide portion of the algorithm. If the list we receive has only a single
element in it, the list can be considered sorted and we can return immediately. This is our recursion base case.
If we have more than 1 element we need to split the list into equal halves and call MergeSort again for each half.

Conquer
Once you have split the list down to single elements, your mergesort will start merging lists, in order, until you have
reassembled the entire list in order.
"""
from asserts.asserts import assert_


def merge_sort(array):
    _merge_sort(array, 0, len(array)-1)


def _merge_sort(array, start, end):
    if (end - start + 1) <= 1:
        return

    m = (start + end) // 2
    _merge_sort(array, start, m)
    _merge_sort(array, m+1, end)
    merge(array, start, m, m+1, end)


def merge(array, start1, end1, start2, end2):
    size = end2 - start1 + 1
    sorted_array = [0] * size

    index1 = start1
    index2 = start2
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

    for index in sorted_array:
        array[index] = sorted_array[index]


def tests():
    array = [0, 1, 3, -1, 2]
    merge(array, 0, 2, 3, 4)
    assert_(expected=[-1, 0, 1, 2, 3], actual=array)


tests()