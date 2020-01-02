from redblacktrees.red_black_bst import *
from asserts.asserts import assert_


def tests():
    tree = RedBlackTree()
    # Test insert
    tree.insert(2)
    tree.insert(3)
    tree.insert(1)
    tree.insert(0)

    in_order_expected = [0, 1, 2, 3]
    in_order_actual = tree.in_order_traversal()
    assert_(in_order_expected, in_order_actual)

    tree = RedBlackTree()
    tree.insert(9)
    tree.insert(6)
    tree.insert(19)
    tree.insert(13)
    tree.insert(16)
    # print(tree)
    in_order_expected = [6, 9, 13, 16, 19]
    in_order_actual = tree.in_order_traversal()
    assert_(expected=in_order_expected, actual=in_order_actual)

    assert_(expected=True, actual=tree.search(16))
    assert_(expected=True, actual=tree.search(19))
    assert_(expected=True, actual=tree.search(6))
    assert_(expected=False, actual=tree.search(31))
tests()