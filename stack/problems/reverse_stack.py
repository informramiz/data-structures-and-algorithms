"""
Problem Statement
Reverse a stack. If your stack initially has 1, 2, 3, 4 (4 at the top and 1 at the bottom),
after reversing the order must be 4, 3, 2, 1 (4 at the bottom and 1 at the top).
"""

from stack.stack_with_native_list import Stack
from asserts.asserts import assert_


def reverse_stack_using_queue(stack: Stack):
    """
    Reverse a given input stack

    Args:
       stack(stack): Input stack to be reversed
    Returns:
       stack: Reversed Stack
    """
    if stack is None or stack.is_empty():
        return stack

    queue = []
    while not stack.is_empty():
        queue.append(stack.pop())

    while len(queue) > 0:
        stack.push(queue.pop(False))

    return stack


def build_stack(arr):
    stack = Stack()
    for value in arr:
        stack.push(value)
    return stack


def stack_to_list(stack: Stack):
    arr = []
    while not stack.is_empty():
        arr.insert(0, stack.pop())
    return arr


def test_reverse_stack():
    output = reverse_stack_using_queue(build_stack([1, 2, 3, 4]))
    assert_([4, 3, 2, 1], stack_to_list(output))

    output = reverse_stack_using_queue(build_stack([1]))
    assert_([1], stack_to_list(output))


test_reverse_stack()
