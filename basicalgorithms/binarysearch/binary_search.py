"""
Binary search practice
Let's get some practice doing binary search on an array of integers. We'll solve the problem two
different ways—both iteratively and recursively.

Here is a reminder of how the algorithm works:

Find the center of the list (try setting an upper and lower bound to find the center)
Check to see if the element at the center is your target.
If it is, return the index.
If not, is the target greater or less than that element?
If greater, move the lower bound to just above the current center
If less, move the upper bound to just below the current center
Repeat steps 1-6 until you find the target or until the bounds are the same
or cross (the upper bound is less than the lower bound).

Problem statement:
Given a sorted array of integers, and a target value, find the index of the target value in the array.
If the target value is not present in the array, return -1.
"""


def binary_search_iterative_bounded(array, key, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == key:
            return mid
        elif key < array[mid]:
            #  key is in the first half
            end = mid-1
        else:
            # key is in the second half
            start = mid + 1

    return -1


def binary_search_iterative(array, key):
    start = 0
    end = len(array) - 1
    return binary_search_iterative_bounded(array, key, start, end)


def binary_search_recursive(array, key):
    return _binary_search_recursive(array, key, 0, len(array)-1)


def _binary_search_recursive(array, key, start_index, end_index):
    if start_index > end_index:
        return -1

    mid = (start_index + end_index) // 2
    if array[mid] == key:
        return key
    elif key < array[mid]:
        # key is in first half
        return _binary_search_recursive(array, key, start_index, end_index-1)
    else:
        # key is in second half
        return _binary_search_recursive(array, key, start_index+1, end_index)