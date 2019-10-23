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


def test_stack_pop():
    foo_stack = Stack()
    foo_stack.push("Test1")
    foo_stack.push("Test2")
    top = foo_stack.pop()
    assert top == "Test2", f"top is: {top}"


test_stack_pop()


def test_stack_top():
    foo_stack = Stack()
    foo_stack.push("Test1")
    foo_stack.push("Test2")
    top = foo_stack.top()
    # top should remain same as before
    top = foo_stack.top()
    assert top == "Test2", f"top is: {top}"


test_stack_top()


def test_stack_is_empty():
    foo_stack = Stack()
    foo_stack.push("Test1")
    foo_stack.push("Test2")
    foo_stack.pop()
    foo_stack.pop()
    assert foo_stack.is_empty() is True


test_stack_is_empty()