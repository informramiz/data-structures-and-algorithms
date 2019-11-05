"""
Problem Statement
You have been given an array containg numbers. Find and return the largest sum in a contiguous subarray within the input array.

Example 1:

arr= [1, 2, 3, -4, 6]
The largest sum is 8, which is the sum of all elements of the array.
Example 2:

arr = [1, 2, -5, -4, 1, 6]
The largest sum is 7, which is the sum of the last two elements of the array.
"""


def max_sum_subarray(array):
    running_sum = array[0]
    max_sum = running_sum
    for n in array[1:]:
        # keep previous array if adding new element n results in greater sum than the number itself
        # otherwise start the new array from this number n
        running_sum = max(running_sum + n, n)
        max_sum = max(running_sum, max_sum)

    return max_sum

def test_max_sum_subarray():
    output = max_sum_subarray([1, 2, 3, -4, 6])
    assert output == 8, f"output: {output}"
    output = max_sum_subarray([1, 2, -5, -4, 1, 6])
    assert output == 7, f"output: {output}"

    output = max_sum_subarray([-12, 15, -13, 14, -1, 2, 1, -5, 4])
    assert output == 18, f"output: {output}"

    output = max_sum_subarray([-1, -1, -2])
    assert output == -1, f"output: {output}"

test_max_sum_subarray()