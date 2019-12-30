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
        current_node = self.root
        for char in word:
            if char not in current_node:
                return False
            current_node = current_node.children[char]

        return current_node.is_word

    def __repr__(self):
        return str(self.to_list(self.root, ""))

    def to_list(self, node, word):
        if node is None:
            return []

        words = []
        for child_key in node:
            child_node = node.children[child_key]
            if child_node.is_word:
                words.append(word + child_key)

            words += (self.to_list(child_node, word + child_key))

        return words

