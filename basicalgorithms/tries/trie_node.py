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

