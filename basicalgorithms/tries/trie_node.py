class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

    def __iter__(self):
        for key in self.children:
            yield key

    def add(self, char: str):
        self.children[char] = TrieNode()

    def __repr__(self):
        return str([c for c in self])

    def suffixes(self):
        # Recursive function that collects the suffix for
        # all complete words below this point
        return self.__suffixes(self)

    def __suffixes(self, node, word=""):
        if node is None:
            return []

        words = []
        for child_key in node:
            child_node = node.children[child_key]
            if child_node.is_word:
                words.append(word + child_key)

            words += self.__suffixes(child_node, word + child_key)
        return words

