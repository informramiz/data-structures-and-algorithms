from LinkedList import LinkedList
from LinkedList import Node

def is_circular(linked_list):
    """
    Determine whether the Linked List is circular or not

    Args:
       linked_list(obj): Linked List to be checked
    Returns:
       bool: Return True if the linked list is circular, return False otherwise

       The way we'll do this is by having two pointers, called "runners", moving
       through the list at different rates. Typically we have a "slow" runner
       which moves at one node per step and a "fast" runner that moves at two
       nodes per step.

       If a loop exists in the list, the fast runner will eventually move behind
       the slow runner as it moves to the beginning of the loop. Eventually it will
       catch up to the slow runner and both runners will be pointing to the same
       node at the same time. If this happens then you know there is a loop in
       the linked list. Below is an example where we have a slow runner
       and a fast runner (the red arrow).
    """
    slow = linked_list.head
    fast = linked_list.head
    #as fast runner will reach end first if there is no loop so
    #adding a None check on just fast should be enough
    while fast and fast.next:
        slow = slow.next
        #move fast runner 2 times to make it fast as compared to slow runner
        fast = fast.next.next

        if fast == slow:
            return True

    # If we get to a node where fast doesn't have a next node or doesn't exist itself,
    # the list has an end and isn't circular
    return False
#test cycle
def test_ls_cycle():
    list_with_loop = LinkedList([2, -1, 3, 0, 5])
    # Creating a loop where the last node points back to the second node
    loop_start = list_with_loop.head.next

    node = list_with_loop.head
    while node.next:
        node = node.next
    node.next = loop_start

    # Test Cases
    small_loop = LinkedList([0])
    small_loop.head.next = small_loop.head
    print ("Pass" if is_circular(list_with_loop) else "Fail")
    print ("Pass" if not is_circular(LinkedList([-4, 7, 2, 5, -1])) else "Fail")
    print ("Pass" if not is_circular(LinkedList([1])) else "Fail")
    print ("Pass" if is_circular(small_loop) else "Fail")
    print ("Pass" if not is_circular(LinkedList([])) else "Fail")
test_ls_cycle()
