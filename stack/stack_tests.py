from stack import Stack


def test_stack_push():
    foo_stack = Stack()
    foo_stack.push(1)
    foo_stack.push(2)
    foo_stack.push(3)
    foo_stack.push(4)
    foo_stack.push(5)
    foo_stack.push(6)
    foo_stack.push(7)
    foo_stack.push(8)
    foo_stack.push(9)
    foo_stack.push(10)  # The array is now at capacity!
    foo_stack.push(11)  # This one should cause the array to increase in size

    assert foo_stack.capacity() == 20, f"Stack capacity: {foo_stack.capacity}"


test_stack_push()