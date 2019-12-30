from basicalgorithms.tries.trie_node import TrieNode
from asserts.asserts import assert_


def tests():
    trie_node = TrieNode()
    trie_node.add("a")
    actual = "a" in trie_node
    assert_(expected=True, actual=actual)


tests()