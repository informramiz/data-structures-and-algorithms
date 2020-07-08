"""
Author: Ramiz Raja
Date: 08/07/2020
"""

codes = {'.-': 'A', '-..': 'D', '.': 'E', '--.':'G', '..': 'I', '-.-': 'K', '--': 'M', '-.': 'N', '---': 'O', '.-.': 'R',
         '...': 'S', '-':'T', '..-':'U','.--':'W'}

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = None

    def __repr__(self):
        return f"Node({self.value})"


class Tree:
    def __init__(self):
        self.root = Node(None)

    def insert(self, code, char):
        node = self.root
        for c in code:
            if c == '.':
                # left
                if node.left:
                    node = node.left
                else:
                    node.left = Node(None)
                    node = node.left
            else:
                # right
                if node.right:
                    node = node.right
                else:
                    node.right = Node(None)
                    node = node.right

        node.value = char

    def find(self, code):
        node = self.root
        for c in code:
            if c == '.':
                # left
                if node.left:
                    node = node.left
                else:
                    return None
            else:
                # right
                if node.right:
                    node = node.right
                else:
                    return None

        return node.value

    def _search(self, node, code, i = 0):
        if i >= len(code):
            return [node]

        c = code[i]
        nodes = []
        if c == '.':
            nodes += self._search(node.left, code, i+1)
        elif c == '-':
            nodes += self._search(node.right, code, i+1)
        else:
            nodes += self._search(node.left, code, i+1)
            nodes += self._search(node.right, code, i+1)

        return nodes

    def search_with_question_mark(self, code):
        return [node.value for node in self._search(self.root, code)]

    def intelligent_search(self, signals):
        characters = []
        if signals.find('?') == -1:
            characters += self.find(signals)
        else:
            characters += self.search_with_question_mark(signals)

        return characters

    def pre_order_traversal(self):
        return self._pre_order_traversal(self.root)

    def _pre_order_traversal(self, node):
        #parent first order
        output = [node.value]
        if node.left:
            output += self._pre_order_traversal(node.left)
        if node.right:
            output += self._pre_order_traversal(node.right)

        return output


def build_tree():
    tree = Tree()
    for key, item in codes.items():
        tree.insert(key, item)

    return tree

def resolve_questions(code):
    count = 0
    code_size = len(code)
    for c in code:
        if c == '?':
            count += 1

    if count == 0:
        return [code]

code_tree = build_tree()

def possibilities(signals):
    if len(signals) == 0:
        return ""

    return code_tree.intelligent_search(signals)


# print(possibilities(['.']))
# print(possibilities('.-'))
print(possibilities('?.'))
print(possibilities('.?'))


def read_number(str, i = 0):
    # skip space if any
    if str[i] == ' ':
        i += 1

    sign_value = 1
    if str[i] == '-':
        sign_value *= -1
        i += 1

    value = ""
    while i < len(str) and (str[i] == '.' or str[i].isdigit()):
        value += str[i]
        i += 1

    digit_value = 0
    if value.find('.') != -1:
        digit_value = float(value)
    else:
        digit_value = int(value)

    return sign_value * digit_value, i-1

def read_number_intelligent(str, i = 0):
    # skip space if any
    if str[i] == ' ':
        i += 1

    sign_value = 1
    if str[i] == '-':
        sign_value *= -1

    is_open_parenthesis = False
    if str[i] == '(':
        is_open_parenthesis = True
        i += 1

    number, i = read_number(str, i)
    if is_open_parenthesis:
        while str[i] != ')':
            i += 1

        return number * sign_value, i

    return sign_value * number, i


def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    if operator == '*' or operator == '/':
        return 2
    return 0

def apply_operator(n1, n2, operator):
    if operator == '+':
        return n1 + n2
    if operator == '-':
        return n1 - n2
    if operator == '*':
        return n1 * n2
    if operator == '/':
        return n1 // n2

def calc(expression):
    value_stack = []
    operator_stack = []

    i = 0
    was_last_operator_open_paranthesis = False
    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue

        print(expression[i])

        if expression[i] == '(':
            was_last_operator_open_paranthesis = True
            operator_stack.append(expression[i])
        elif expression[i].isdigit() or (was_last_operator_open_paranthesis and expression[i] == '-') or (i == 0 and expression[i] == '-'):
            was_last_operator_open_paranthesis = False
            number, i = read_number(expression, i)
            print(number)
            value_stack.append(number)
        elif expression[i] == ')':
            was_last_operator_open_paranthesis = False
            while len(operator_stack) != 0 and operator_stack[-1] != '(':
                n1 = value_stack.pop()
                n2 = value_stack.pop()
                operator = operator_stack.pop()
                value_stack.append(apply_operator(n2, n1, operator))

            operator_stack.pop()
        else:
            was_last_operator_open_paranthesis = True
            while (len(operator_stack) != 0 and
                   precedence(operator_stack[-1]) >= precedence(expression[i])):
                n1 = value_stack.pop()
                n2 = value_stack.pop()
                operator = operator_stack.pop()
                value_stack.append(apply_operator(n2, n1, operator))

            operator_stack.append(expression[i])

        i += 1

    while len(operator_stack) != 0:
        n1 = value_stack.pop()
        n2 = value_stack.pop()
        operator = operator_stack.pop()
        value_stack.append(apply_operator(n2, n1, operator))

    return value_stack[-1]


# print(calc("123.45*(678.90 / (-2.5+ 11.5)-(80 -19) *33.25) / 20 + 11"))
# print(calc("(123.45*(678.90 / (-2.5+ 11.5)-(((80 -(19))) *33.25)) / 20) - (123.45*(678.90 / (-2.5+ 11.5)-(((80 -(19))) *33.25)) / 20) + (13 - 2)/ -(-11)"))
print(calc("-12 * -123"))