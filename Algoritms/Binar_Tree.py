import random


class Node:
    count = 0

    def __init__(self, val):
        Node.count += 1
        self.left = None
        self.right = None
        self.value = val
        self.id = Node.count


class Tree:
    count = 0

    def __init__(self):
        """
        Create Tree
        """
        # For ID tree, NOT USEFUL
        Tree.count += 1
        self.id = Tree.count
        # FIRST inincialization root of tree is None
        # first Tree.add root is not None
        self.root: Node = None

    def add(self, val):
        """
        Add value to tree
        :param val: value, type INT
        :return:
        """
        if not isinstance(val, int):
            raise TypeError("Value in Tree must be ONLY INT")
        if self.root is not None:
            self._add(val, self.root)
        else:
            self.root = Node(val)

    def _add(self, val: int, node: Node):
        """
        Recursion function to add value in Tree
        :param val: value, type INT
        :param node: node, type Node
        :return: None
        """
        if val < node.value:
            if node.left is None:
                node.left = Node(val)
            else:
                self._add(val, node.left)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self._add(val, node.right)

    def find(self, val):
        """
        Find value in Tree
        :param val: value
        :return: None or Node (if val in tree)
        """
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val: int, node: Node):
        """
        Recursion function to find value in Tree
        :param val: value
        :param node: Node
        :return: None or Node (if val in tree)
        """
        if val == node.value:
            return node
        elif val < node.value and node.left is not None:
            return self._find(val, node.left)
        elif val > node.value and node.right is not None:
            return self._find(val, node.right)
        else:
            return None

    def printTree(self):
        """
        Print Tree
        :return: None
        """
        self._printTree(self.root)

    def _printTree(self, node: Node, level=0):
        """
        Recursion function to print all Nodes of Tree
        :param node: Node
        :param level: DON'T touch it, use only for dedent
        :return: None
        """
        if node is not None:
            indent = level * "\t"
            print(f"{indent}Id: {node.id}, value: {node.value}")
            self._printTree(node.left, level=level + 1)
            self._printTree(node.right, level=level + 1)

    def printOrderAdder(self):
        """
        Print ordered Nodes (by Node.id) in Tree
        :return: None
        """
        if self.root is not None:
            self._printOrderAdder(self.root)

    def _printOrderAdder(self, node: Node):
        """
        Recursion function to print ordered Nodes (by Node.id) in Tree
        :param node: Node
        :return: None, only print all orderd Nodes (by Node.id) in Tree
        """
        if node is not None:
            pass
            # TODO: print order Nodes of Tree


def find_node(value: int, tree: Tree):
    """
    Find value in Tree
    :param value: value
    :param tree: Tree
    :return: Node or None
    """
    find: Node = tree.find(value)
    if find is not None:
        print(f"Find node {find.id} with value {find.value}") \
                return find
    else:
        print(f"Value {value} not in tree {tree.id}")
        return None


tree = Tree()
tree.add(5)
for _ in range(10):
    tree.add(random.randint(1, 10))

tree.printTree()
find_node(7, tree)
