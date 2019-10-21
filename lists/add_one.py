"""
------------Problem Statement---------
You are given a non-negative number in the form of list elements. For example, the number 123 would be provided as arr = [1, 2, 3]. Add one to the number and return the output in the form of a new list.

Example 1:

input = [1, 2, 3]
output = [1, 2, 4]
Example 2:

input = [9, 9, 9]
output = [1, 0, 0, 0]

Solution-1:
One way to solve this problem is to convert the input array into a number and then add one to it.
For example, if we have input = [1, 2, 3], you could solve this problem by creating the number
123 and then separating the digits of the output number 124.

Solution-2, Efficient:
Just add 1 the way we humans add 1 to any value. Start from the end value, add 1 to it and then keep carry/borrow
if needed and keep adding the carry to remaining values
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
    """
    One way to solve this problem is to convert the input array into a number and then add one to it.
    For example, if we have input = [1, 2, 3], you could solve this problem by creating the number
    123 and then separating the digits of the output number 124.
    """
    if len(array) == 0:
        return ['1']

    decimal = convert_array_to_decimal(array)
    decimal += 1
    output = convert_decimal_to_array(decimal)
    return output

def add_one_efficient(array):
    """
    Just add 1 the way we humans add 1 to any value. Start from the end value, add 1 to it and then keep carry/borrow
    if needed and keep adding the carry to remaining values
    """

    # at start the carry will be 1 as we want to add 1
    carry = 1
    # run loop in reverse range [start = n-1, end = -1 (exclusive), step = -1)
    for i in range(len(array)-1, -1, -1):
        output = carry + array[i]
        carry = output // 10
        array[i] = output % 10

    # at the end if there is still carry then prepend it, example: 99 + 1 = 100, in this carry goes to start
    if carry > 0:
        array = [carry] + array

    return array

def test_add_one(test_case, add_one):
    arr = test_case[0]
    solution = test_case[1]

    output = add_one(arr)
    assert output == solution, f"output: {output}"


def run_test_cases(add_one):
    # Test case-1
    arr = [0]
    solution = [1]
    test_case = [arr, solution]
    test_add_one(test_case, add_one)

    # Test case-2
    arr = [1, 2, 3]
    solution = [1, 2, 4]
    test_case = [arr, solution]
    test_add_one(test_case, add_one)

    # Test case-3
    arr = [9, 9, 9]
    solution = [1, 0, 0, 0]
    test_case = [arr, solution]
    test_add_one(test_case, add_one)


# run test cases on normal `add_one()`
run_test_cases(add_one)
# run test cases on `add_one_efficient()`
run_test_cases(add_one_efficient)