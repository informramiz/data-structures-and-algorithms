"""
Author: Ramiz Raja
Created on: 07/01/2020

--> Heapsort:
A heapsort is an in-place sorting algorithm that treats an array like a binary tree and moves the largest values to
the end of the heap until the full array is sorted.

The main steps in a heapsort are:

1. Convert the array into a maxheap (a complete binary tree with decreasing values)
2. Swap the top element with the last element in the array (putting it in it's correct final position)
3. Repeat with arr[:len(arr)-1] (all but the sorted elements)
"""
from asserts.asserts import assert_


def heap_sort(array):
    # convert array into max-heap
    n = len(array)
    for i in range(n-1, -1, -1):
        heapify_down(array, i, n)

    # swap max element at the end and call heapify again repeatedly
    for i in range(n-1, -1, -1):
        # Remove max element from heap: involves following 2 steps
        # 1. swap max element (array[0]) with element at last
        array[0], array[i] = array[i], array[0]
        # 2. heapify the root element (array[0] is always the root in a heap) till the i-1 index or n = i size
        heapify_down(array, 0, i)


def heapify_down(array, parent, n):
    while parent < n:
        left = 2 * parent + 1
        right = 2 * parent + 2
        max_index = parent

        if left < n and array[left] > array[parent]:
            max_index = left

        if right < n and array[right] > array[max_index]:
            max_index = right

        if max_index != parent:
            # swap parent with child that has maximum value (max_index child)
            array[parent], array[max_index] = array[max_index], array[parent]
            # now check on the child
            parent = max_index
        else:
            # parent is fine so no need to check down
            break


def tests():
    array = [3, 1, 2, 0, 2, -1]
    heap_sort(array)
    assert_(expected=[-1, 0, 1, 2, 2, 3], actual=array)

    array = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
    solution = [0, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]
    heap_sort(array)
    assert_(expected=solution, actual=array)

    array = [5, 5, 5, 3, 3, 3, 4, 4, 4, 4]
    solution = [3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
    heap_sort(array)
    assert_(expected=solution, actual=array)

    array = [99]
    solution = [99]
    heap_sort(array)
    assert_(expected=solution, actual=array)

    array = [0, 1, 2, 5, 12, 21, 0]
    solution = [0, 0, 1, 2, 5, 12, 21]
    heap_sort(array)
    assert_(expected=solution, actual=array)

tests()