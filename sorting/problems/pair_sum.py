"""
Author: Ramiz Raja
Created on: 09/01/2020
Problem: Given an input array and a target value (integer), find two values in the array whose sum is equal to the
target value. Solve the problem without using extra space. You can assume the array has unique values and will
never have more than one solution.
"""
from asserts.asserts import assert_


def pair_sum(array, target):
    array.sort()

    front_index = 0
    back_index = len(array)-1
    while front_index < back_index:
        front = array[front_index]
        back = array[back_index]
        if front + back == target:
            return [front, back]
        elif front + back < target:
            # increase by minimum amount which is next front as array is sorted
            front_index += 1
        else:
            # front + back > target, decrease by minimum amount which is taking the next maximum element less than back
            back_index -= 1

    return [None, None]


def tests():
    input_list = [2, 7, 11, 15]
    target = 9
    solution = [2, 7]
    assert_(expected=solution, actual=pair_sum(input_list, target))

    input_list = [0, 8, 5, 7, 9]
    target = 9
    solution = [0, 9]
    assert_(expected=solution, actual=pair_sum(input_list, target))

    input_list = [110, 9, 89]
    target = 9
    solution = [None, None]
    assert_(expected=solution, actual=pair_sum(input_list, target))


tests()