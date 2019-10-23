from queue_with_stacks import Queue


def test_queue_with_stacks_tests():
    # Setup
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    # Test size
    assert(q.size() == 3)

    # Test dequeue
    assert(q.dequeue() == 1)

    # Test enqueue
    q.enqueue(4)
    assert (q.dequeue() == 2)
    assert (q.dequeue() == 3)
    assert (q.dequeue() == 4)
    q.enqueue(5)
    assert (q.size() == 1)


test_queue_with_stacks_tests()