"""
Author: Ramiz Raja
Created on: 03/01/2020
"""

from asserts.asserts import assert_


def case_specific_sorting(string):
    if len(string) == 0:
        return string

    copy = string
    sorted_str = sorted(copy)
    lower_case_index = 0
    size = len(string)
    while lower_case_index < size and not sorted_str[lower_case_index].islower():
        lower_case_index += 1

    upper_case_index = 0
    output = [''] * size
    for i in range(size):
        if string[i].isupper():
            output[i] = sorted_str[upper_case_index]
            upper_case_index += 1
        else:
            output[i] = sorted_str[lower_case_index]
            lower_case_index += 1

    return ''.join(output)


def tests():
    test_string = 'fedRTSersUXJ'
    output = case_specific_sorting(test_string)
    assert_(expected="deeJRSfrsTUX", actual=output)

    test_string = "defRTSersUXI"
    output = case_specific_sorting(test_string)
    assert_(expected="deeIRSfrsTUX", actual=output)

tests()