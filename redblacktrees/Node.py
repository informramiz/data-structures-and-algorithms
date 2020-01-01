"""
The Node class will need a couple new attributes. It is no longer enough to only know the children,
because we need to ask questions during insertion like, "what color is my parent's sibling?".
So we will add a parent link as well as the color.
"""
from redblacktrees.Color import Color


class Node(object):
    def __init__(self, value, parent, color: Color = Color.RED):
        self.value = value
        self.parent = parent
        self.color = color
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.value}, {self.color})"
