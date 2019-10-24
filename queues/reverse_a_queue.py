from queue_with_python_list import Queue
from stack.stack_with_native_list import Stack


def reverse_queue(queue=Queue()):
    """
        Reverse the input queue

        Args:
           queue(queue),str2(string): Queue to be reversed
        Returns:
           queue: Reversed queue
    """
    stack = Stack()
    while not queue.is_empty():
        stack.push(queue.dequeue())

    while not stack.is_empty():
        queue.enqueue(stack.pop())


def run_test_case(test_case):
    queue = Queue()
    for num in test_case:
        queue.enqueue(num)

    reverse_queue(queue)
    index = len(test_case) - 1
    while not queue.is_empty():
        removed = queue.dequeue()
        assert removed == test_case[index], f"removed={removed}, test case={test_case[index]}"
        index -= 1


def test_reverse_queue():
    test_case_1 = [1, 2, 3, 4]
    run_test_case(test_case_1)

    test_case_2 = [1]
    run_test_case(test_case_2)

test_reverse_queue()
