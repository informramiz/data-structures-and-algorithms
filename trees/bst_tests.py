from BST import BST
from BST import Node


def test_BST():
    bst = BST()

    # Test empty tree
    assert (len(bst.BFS()) == 0)

    # Test insert
    bst.insert(2)
    bst.insert(3)
    bst.insert(1)
    assert (len(bst.BFS()) == 3)
    expected = [2, 1, 3]
    actual = [node.value for node,l in bst.BFS()]
    assert expected == actual, f"expected={expected}, actual={actual}"

    # Test search
    assert(bst.search(2) is True)
    assert(bst.search(5) is False)

test_BST()