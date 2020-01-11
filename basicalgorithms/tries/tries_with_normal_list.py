"""
Implement two functions for the Trie class below. Implement add to add a word to the Trie.
Implement exists to return True if the word exist in the trie and False if the word doesn't exist in the trie.
"""

from basicalgorithms.tries.trie_node import TrieNode


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add `word` to trie
        """
        current_node = self.root
        for char in word:
            if char not in current_node:
                current_node.add(char)

            current_node = current_node.children[char]

        current_node.is_word = True

    def exists(self, word):
        """
        Check if word exists in trie
        """
        node = self.find(word)
        if node:
            return node.is_word
        else:
            return False

    def find(self, prefix):
        """
        Find the node with the prefix
        """
        current_node = self.root
        for char in prefix:
            if char not in current_node:
                return None
            current_node = current_node.children[char]

        return current_node

    def __repr__(self):
        return str(self.to_list())

    def to_list(self):
        if self.root is None:
            return []
        return self.root.suffixes()

