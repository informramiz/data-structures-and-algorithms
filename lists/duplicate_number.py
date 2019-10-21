"""
Problem Statement
You have been given an array of length = n. The array contains integers from 0 to n - 2. Each number in the array is
present exactly once except for one number which is present twice.
Find and return this duplicate number present in the array

Example:

arr = [0, 2, 3, 1, 4, 5, 3]
output = 3 (because 3 is present twice)
The expected time complexity for this problem is O(n) and the expected space-complexity is O(1).
"""


def find_duplicate_number(array):
    """
    We know that we will be given a series of numbers [0, n-2] with one extra number (the duplicate number)
    so if we take the total sum of series [0, n-2] (arithmetic series sum = n((a1 + an)/2) ) and extract it
    from actual sum of the array we we will get the extra number
    :param array:
    :return: duplicate number
    """

    # total terms
    n = ((len(array)-2) + 1) # +1 to include 0 as the range is [0, n-2] with 0 inclusive
    # first term
    a1 = 0
    # last term
    an = len(array)-2
    # arithmetic series total sum = n((a1 + an)/2
    expected_sum = n * (a1 + an) / 2
    actual_sum = sum(array) # this will be greater than expected sum as there is an extra duplicate number
    return actual_sum - expected_sum # this will give the duplicate number as that number is extra


def test_find_duplicate_number():
    output = find_duplicate_number([0, 0])
    assert output == 0, f"output: {output}"

    output = find_duplicate_number([0, 2, 3, 1, 4, 5, 3])
    assert output == 3, f"output: {output}"

    output = find_duplicate_number([0, 1, 5, 4, 3, 2, 0])
    assert output == 0, f"output: {output}"

    output = find_duplicate_number([0, 1, 5, 5, 3, 2, 4])
    assert output == 5, f"output: {output}"


test_find_duplicate_number()
