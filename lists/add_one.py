"""
------------Problem Statement---------
You are given a non-negative number in the form of list elements. For example, the number 123 would be provided as arr = [1, 2, 3]. Add one to the number and return the output in the form of a new list.

Example 1:

input = [1, 2, 3]
output = [1, 2, 4]
Example 2:

input = [9, 9, 9]
output = [1, 0, 0, 0]

Solution:
One way to solve this problem is to convert the input array into a number and then add one to it.
For example, if we have input = [1, 2, 3], you could solve this problem by creating the number
123 and then separating the digits of the output number 124.
"""


def convert_array_to_decimal(array):
    # Given input ['1', '2', '3'], the output will be
    # decimal = 1*10^2 + 2*10^1 + 3*10^0 = 123
    decimal = 0
    power = len(array) - 1
    for value in array:
        decimal += value * pow(10, power)
        power -= 1

    return decimal


def test_convert_array_to_decimal():
    assert(convert_array_to_decimal([1, 2, 3]) == 123)


test_convert_array_to_decimal()


def convert_decimal_to_array(decimal):
    array = []
    while decimal > 0:
        result = decimal % 10
        decimal = int(decimal / 10)
        array.insert(0, result)

    return array


def test_convert_decimal_to_array():
    assert(convert_decimal_to_array(123) == [1, 2, 3])


test_convert_decimal_to_array()


def add_one(array):
    if len(array) == 0:
        return ['1']

    decimal = convert_array_to_decimal(array)
    decimal += 1
    output = convert_decimal_to_array(decimal)
    return output


assert (add_one([1, 2, 3]) == [1, 2, 4])
assert (add_one([1, 2, 9]) == [1, 3, 0])


def test_add_one(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = add_one(arr)
    assert output == solution, f"output: {output}"


# Test case-1
arr = [0]
solution = [1]
test_case = [arr, solution]
test_add_one(test_case)


# Test case-2
arr = [1, 2, 3]
solution = [1, 2, 4]
test_case = [arr, solution]
test_add_one(test_case)


# Test case-3
arr = [9, 9, 9]
solution = [1, 0, 0, 0]
test_case = [arr, solution]
test_add_one(test_case)