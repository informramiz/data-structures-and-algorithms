from basicalgorithms.tries.tries_with_normal_list import *
from asserts.asserts import assert_


def test():
    trie = Trie()
    trie.add("hello")
    trie.add("hey")
    trie.add("add")

    assert_(True, trie.exists("hello"))
    assert_(True, trie.exists("hey"))
    assert_(True, trie.exists("add"))
    assert_(False, trie.exists("RR"))


test()
