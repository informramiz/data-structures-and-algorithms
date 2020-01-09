"""
Author: Ramiz Raja
Created on: 10/01/2020
Problem: Write a function that takes an input array (or Python list) consisting of only 0s, 1s, and 2s,
and sorts that array in a single traversal.
"""
from asserts.asserts import assert_


def sort_0s_1s_2s(array):
    next_index_0 = 0
    next_index_2 = len(array) - 1
    front_index = 0
    while front_index <= next_index_2:
        # Trick: front_index will only move if a[front_index] == 0 or a[front_index] == 1 to make sure front
        # of array is 0s followed by 1s, if a[front_index] == 2 then it will not move so that we can check
        # on next iteration that the a[front_index]'s new value is valid.

        if array[front_index] == 0:
            # move it on the left by swapping (front_index, next_index_0)
            array[front_index] = array[next_index_0]
            array[next_index_0] = 0
            front_index += 1
            next_index_0 += 1
        elif array[front_index] == 2:
            # move it to the right by swapping (front_index, next_index_2)
            array[front_index] = array[next_index_2]
            array[next_index_2] = 2
            next_index_2 -= 1
            # front_index will not move in this case because the new value of a[front_index] may be 0 or 2 and we need
            #  to check and handle it accordingly. This check will be done automatically if we don't move front_index
            # in this iteration
        else:
            # array[front_index] == 1, keep skipping ones until you encounter another 0 or 1
            # because we are only swapping 0s and 2s and it will automatically bring 1s to their right position
            front_index += 1


def tests():
    test_case = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
    sort_0s_1s_2s(test_case)
    assert_(expected=sorted(test_case), actual=test_case)

    test_case = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
    sort_0s_1s_2s(test_case)
    assert_(expected=sorted(test_case), actual=test_case)

    test_case = [2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1]
    sort_0s_1s_2s(test_case)
    assert_(expected=sorted(test_case), actual=test_case)


tests()

