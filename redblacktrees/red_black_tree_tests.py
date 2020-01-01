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
    print(tree)


tests()