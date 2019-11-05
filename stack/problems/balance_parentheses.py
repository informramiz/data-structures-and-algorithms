"""
Balanced Parentheses Exercise
In this exercise you are going to apply what you learned about stacks with a real world problem. We will be using stacks
 to make sure the parentheses are balanced in mathematical expressions such as:

 ((32+8)∗(5/2))/(2+6).

In real life you can see this extend to many things such as text editor plugins and interactive development
environments for all sorts of bracket completion checks.

Take a string as an input and return True if it's parentheses are balanced or False if it is not.
"""

from stack.stack_with_native_list import Stack


def is_opening_parentheses(char):
    return char in "[({"


def is_closing_parentheses(char):
    return char in "])}"


def is_parentheses(char):
    return is_opening_parentheses(char) or is_closing_parentheses(char)


def check_parentheses_pair(opening, closing):
    if opening == '(' and closing == ')':
        return True
    elif opening == '[' and closing == ']':
        return True
    elif opening == '{' and closing == '}':
        return True

    return False


def equation_checker(equation: str):
    """
    Check equation for balanced parentheses

    Args:
       equation(string): String form of equation
    Returns:
       bool: Return if parentheses are balanced or not
    """
    if equation is None or len(equation) == 0:
        return True

    stack = Stack()
    for char in equation:
        if is_opening_parentheses(char):
            stack.push(char)
        elif is_closing_parentheses(char):
            if stack.is_empty() or check_parentheses_pair(stack.pop(), char) is False:
                return False

    return stack.is_empty()


def test_case(inputt, expected_output):
    actual_output = equation_checker(inputt)
    assert expected_output == actual_output, f"expected={expected_output}, actual={actual_output}"


def test():
    equation = '((3^2 + 8)*(5/2))/(2+6)'
    test_case(equation, True)

    equation = '((3^2 + 8)*(5/2))/(2+6))'
    test_case(equation, False)

    equation = '()'
    test_case(equation, True)

    equation = ''
    test_case(equation, True)

    equation = '({])'
    test_case(equation, False)

    equation = '([{'
    test_case(equation, False)
    print("----All Test cases passed----")

test()