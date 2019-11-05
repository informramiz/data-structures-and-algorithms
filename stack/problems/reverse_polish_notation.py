"""
Reverse Polish Notation
Reverse Polish notation, also referred to as Polish postfix notation is a way of laying out operators and operands.

When making mathematical expressions, we typically put arithmetic operators (like +, -, *, and /) between operands.
For example: 5 + 7 - 3 * 8

However, in Reverse Polish Notation, the operators come after the operands. For example: 3 1 + 4 *

The above expression would be evaluated as (3 + 1) * 4 = 16

The goal of this exercise is to create a function that does the following:

Given a postfix expression as input, evaluate and return the correct final answer.
Note: In Python 3, the division operator / is used to perform float division. So for this problem, you should use int()
after every division to convert the answer to an integer.

For further reading: http://www.cs.csi.cuny.edu/~zelikovi/csc326/data/assignment5.htm
"""

from stack.stack_with_native_list import Stack
from asserts.asserts import assert_


def evaluate_operator(left_operand, right_operand, operator):
    left_operand = int(left_operand)
    right_operand = int(right_operand)

    if operator == '+':
        return left_operand + right_operand
    elif operator == '-':
        return left_operand - right_operand
    elif operator == 'x':
        return left_operand * right_operand
    else:
        return int(left_operand / right_operand)


def test_evaluate_operator():
    assert_(3, evaluate_operator('2', '1', '+'))
    assert_(3, evaluate_operator('2', '-1', '-'))
    assert_(1, evaluate_operator('2', '1', '-'))
    assert_(2, evaluate_operator('2', '1', '*'))
    assert_(2, evaluate_operator('2', '1', '/'))


test_evaluate_operator()
