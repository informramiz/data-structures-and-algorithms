"""
Author: Ramiz Raja
Created on: 07/01/2020
"""
from asserts.asserts import assert_


def quick_sort(array):
    _quick_sort(array, 0, len(array)-1)


def _quick_sort(array, start, end):
    if start >= end:
        return

    pivot = _balance_the_pivot(array, start, end)

    _quick_sort(array, start, pivot-1)
    _quick_sort(array, pivot+1, end)


def _balance_the_pivot(array, start, end):
    """
    Move all elements greater than pivot to right side of pivot and all elements less than pivot to the left side
    :param array:
    :param start:
    :param end:
    :return: The updated position of pivot in which array is: [elements on left <= pivot element < all elements on right]
    """
    i = start
    pivot = end
    while i < pivot:
        if array[i] > array[pivot]:
            # Move i to pivot, pivot-1 to i and pivot to pivot-1
            p_value = array[pivot]

            # move i to pivot
            array[pivot] = array[i]
            # move pivot-1 to i
            array[i] = array[pivot - 1]
            # move pivot to pivot-1
            array[pivot - 1] = p_value
            pivot -= 1
        else:
            i += 1
    return pivot


def tests():
    array = [4, 3, 1, 4, 3, 3, 2, 4]
    quick_sort(array)
    assert_(expected=[1, 2, 3, 3, 3, 4, 4, 4], actual=array)

    array = [8, 3, 1, 7, 0, 10, 2]
    quick_sort(array)
    assert_(expected=[0, 1, 2, 3, 7, 8, 10], actual=array)

    array = [1, 0]
    quick_sort(array)
    assert_(expected=[0, 1], actual=array)

    array = [96, 97, 98]
    quick_sort(array)
    assert_(expected=[96, 97, 98], actual=array)


tests()
