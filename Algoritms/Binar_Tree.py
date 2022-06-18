__all__ = ["Node",
           "Tree",
           ]
import random


class Node:
    """
    Structure of Node:
    count - need for id None
    left - link to left Node
    right - link to right Node
    value - value of Node
    id - Id of Node
    """
    count = 0

    def __init__(self, val):
        Node.count += 1
        self.left = None
        self.right = None
        self.value = val
        self.id = Node.count


class Tree:
    """
    Tree class
    """
    count = 0

    def __init__(self):
        """
        Create empty Tree
        """
        # For ID tree, NOT USEFUL
        Tree.count += 1
        self.id = Tree.count
        # FIRST inincialization root of tree is None
        # first Tree.add root is not None
        self.root: Node = None
        # Contains array of all nodes, need for print oder nodes, clear after use
        self.tree_nodes = []

    def add(self, val):
        """
        Add value to tree
        :param val: value, type INT
        :return: True
        """
        if not isinstance(val, int):
            raise TypeError("Value in Tree must be ONLY INT")
        if self.root is not None:
            self._add(val, self.root)
        else:
            self.root = Node(val)
            return True

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
        print("Structure of tree")
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
        if self.root is None:
            print("Tree is empty")
            return None
        else:
            print("Order Nodes")
            self._printOrderAdder(self.root)
            self.tree_nodes.sort(key=Tree.sort_array)
            for node in self.tree_nodes:
                if node.right is not None and node.left is not None:
                    print(f"ID: {node.id}, value: {node.value}, right: {node.right.id}, left: {node.left.id}")
                elif node.right is not None and node.left is None:
                    print(f"ID: {node.id}, value: {node.value}, right: {node.right.id}, left: None")
                elif node.right is None and node.left is not None:
                    print(f"ID: {node.id}, value: {node.value}, right: None, left: {node.left.id}")
                else:
                    print(f"ID: {node.id} value: {node.value}, right: None, left: None")
            self.tree_nodes = []

    def _printOrderAdder(self, node: Node):
        """
        Recursion function to print ordered Nodes (by Node.id) in Tree
        :param node: Node
        :return: None, only print all orderd Nodes (by Node.id) in Tree
        """
        if node is not None:
            self.tree_nodes.append(node)
            self._printOrderAdder(node.left)
            self._printOrderAdder(node.right)

    def delete_tree(self):
        """
        Delete link of root
        :return: None
        """
        self.root = None

    def find_node(self, value: int):
        """
        Find value in Tree
        :param value: value
        :param tree: Tree
        :return: Node or None
        """
        find: Node = self.find(value)
        if find is not None:
            print(f"Find node {find.id} with value {find.value}")
            return find
        else:
            print(f"Value {value} not in tree {self.id}")
            return None

    def fill_tree_random(self, num=10, limit_low=1, limit_high=10):
        """
        Add to tree num nodes, value of each other between limit_low and limit_high
        :param num: number of nodes Tree
        :param limit_low: lower value of Tree.value
        :param limit_height: higher value of Tree.value
        :return: result of add nodes to tree
        """
        if self.root is not None:
            return False
        if not isinstance(num, int) or not isinstance(limit_low, int) or not isinstance(limit_high, int):
            raise TypeError("Value must be int")
        if num < 1:
            raise ValueError("Number of tree must be more than 0")
        if limit_low == limit_high or limit_low > limit_high:
            raise ValueError("Incorrect values: limit_low, limit_high")
        for _ in range(0, num):
            self.add(random.randint(limit_low, limit_high))
        return True

    @staticmethod
    def sort_array(node: Node):
        """
        Supportive function to sort tree_nodes
        :param node:
        :return:
        """
        return node.id

if __name__ == "__main__":
    # Example
    tree = Tree()
    tree.add(5)
    for _ in range(10):
        tree.add(random.randint(1, 10))

    tree.printTree()
    tree.find_node(7)
    tree.printOrderAdder()
