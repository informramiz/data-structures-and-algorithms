"""
Author: Ramiz Raja
Created on: 20/01/2020
Problem: Min Operations
Starting from the number 0, find the minimum number of operations required to reach a given positive target number.
 You can only use the following two operations:

1. Add 1
2. Double the number

Example:
For Target = 18, output = 6, because it takes at least 6 steps shown below to reach the target

start = 0
step 1 ==> 0 + 1 = 1
step 2 ==> 1 * 2 = 2 # or 1 + 1 = 2
step 3 ==> 2 * 2 = 4
step 4 ==> 4 * 2 = 8
step 5 ==> 8 + 1 = 9
step 6 ==> 9 * 2 = 18
For Target = 69, output = 9, because it takes at least 8 steps to reach 69 from 0 using the allowed operations

start = 0
step 1 ==> 0 + 1 = 1
step 2 ==> 1 + 1 = 2
step 3 ==> 2 * 2 = 4
step 4 ==> 4 * 2 = 8
step 5 ==> 8 * 2 = 16
step 6 ==> 16 + 1 = 17
step 7 ==> 17 * 2 = 34
step 8 ==> 34 * 2 = 68
step 9 ==> 68 + 1  = 69
"""
from asserts.asserts import assert_


def min_operations(number):
    """
    Return number of steps taken to reach a target number
    number: target number (as an integer)
    :returns: number of steps (as an integer)
    """

    # Solution:
    # 1. The number of steps to reach a target number = number of steps take to make the target number 0
    # 2. We will be greedy, each time if it is possible we will try to make the number half
    steps_count = 0
    while number > 0:
        # check if we can make the number half
        if number % 2 == 0:
            number = number / 2
        else:
            # number can't halved so we can only decrease it by 1
            number -= 1
        steps_count += 1

    return steps_count


def test_function(test_case):
    target = test_case[0]
    solution = test_case[1]
    output = min_operations(target)
    assert_(expected=solution, actual=output)


def tests():
    target = 18
    solution = 6
    test_case = [target, solution]
    test_function(test_case)

    target = 69
    solution = 9
    test_case = [target, solution]
    test_function(test_case)


tests()