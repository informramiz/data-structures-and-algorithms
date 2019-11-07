"""
Given an input string consisting of only { and }, figure out the minimum number of reversals required to make the brackets balanced.

For example:

For input_string = "}}}}, the number of reversals required is 2.
For input_string = "}{}}, the number of reversals required is 1.
If the brackets cannot be balanced, return -1 to indicate that it is not possible to balance them.
"""

from stack.stack_with_native_list import Stack
from asserts.asserts import assert_


def is_opening_bracket(b):
    return b == '{'


assert(is_opening_bracket('{') is True)
assert(is_opening_bracket('}') is False)


def is_closing_bracket(b):
    return b == '}'


assert(is_closing_bracket('}') is True)
assert(is_closing_bracket('{') is False)


def is_correct_bracket_pair(b1, b2):
    return (is_opening_bracket(b1) and is_closing_bracket(b2)) \
           or (is_closing_bracket(b1) and is_opening_bracket(b2))


assert(is_correct_bracket_pair('{', '}') is True)
assert(is_correct_bracket_pair('{', '{') is False)


def get_opposite_bracket(b):
    if is_opening_bracket(b):
        return '}'
    else:
        return '{'


assert(get_opposite_bracket("{") == "}")
assert(get_opposite_bracket("}") == "{")


def count_reversals(stack):
    reversals_count = 0
    while stack.size() > 0:
        # pop the last 2 brackets and try to balance them
        b1 = stack.pop()
        b1_opposite = get_opposite_bracket(b1)
        b2 = stack.pop()
        b2_opposite = get_opposite_bracket(b2)

        # try reversing b1 to see if it is balanced with b2
        if is_correct_bracket_pair(b1_opposite, b2):
            reversals_count += 1
        elif is_correct_bracket_pair(b1, b2_opposite):  # try reversing b2 to see if balanced with b1
            reversals_count += 1
        else:  # b1 and b2 both needs to be reversed to balance them out
            reversals_count += 2
    return reversals_count


def minimum_bracket_reversals(equation: str):
    """
    Calculate the number of reversals to fix the brackets

    Args:
       equation(string): Strings to be used for bracket reversal calculation
    Returns:
       int: Number of bracket reversals needed or -1 if not possible
    """

    # only even length strings can have balanced brackets
    if len(equation) % 2 != 0:
        return -1

    stack = Stack()
    for b in equation:
        if is_opening_bracket(b):
            stack.push(b)
        else:  # closing bracket
            # if current closing bracket is balanced with last bracket then remove last bracket from stack top
            if not stack.is_empty() and is_correct_bracket_pair(b, stack.top()):
                stack.pop()
            else:
                # bracket is not balanced so push it to stack as well
                stack.push(b)

    # remaining brackets on stack are not balanced
    # only even length brackets can be balanced
    if stack.size() % 2 != 0:
        return -1

    reversals_count = count_reversals(stack)
    return reversals_count


def test():
    assert_(2, minimum_bracket_reversals("}}}}"))
    assert_(2, minimum_bracket_reversals("}}{{"))
    assert_(-1, minimum_bracket_reversals("}{{"))
    assert_(2, minimum_bracket_reversals("}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{"))
    assert_(1, minimum_bracket_reversals("}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}"))


test()