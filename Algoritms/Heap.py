__all__ = ["Node", "Heap"]

import random

class Node:
    """
    Simple Node
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Heap:
    def __init__(self):
        self.root = None

    def add(self, value: int) -> bool:
        """
        Add to heap value and new Node
        if added value in heap function add return False
        :param value: value, must be int
        :return: True -> add to heap, False- > no add to heap
        """
        if self.root is None:
            self.root = Node(value)
        else:
            return self._add(value, self.root)

    def _add(self, value: int, node: Node) -> bool:
        """
        Recursion Add to heap value and new Node
        if added value in heap function add return False
        :param value: value, must be int
        :param node: Node
        :return: True -> add to heap, False- > no add to heap
        """
        if value == node.value:
            return False
        if value < node.value and node.left is None:
            node.left = Node(value)
            return True
        elif value < node.value and node.left is not None:
            self._add(value, node.left)
        elif value > node.value and node.right is None:
            node.right = Node(value)
            self._reverse(node, node.right)
            return True
        elif value > node.value and node.right is not None:
            buf_val = node.value
            node.value = value
            self._add(buf_val, node.right)
        else:
            return False

    def _reverse(self, node_1: Node, node_2: Node) -> None:
        """
        Reverse two values between two nodes
        :param node_1: Node 1
        :param node_2: Node 2
        :return: None
        """
        node_1.value, node_2.value = node_2.value, node_1.value

    def show_heap(self) -> None:
        """
        Print in console all heap node
        :return: None
        """
        if self.root is not None:
            self._show_heap(self.root)

    def _show_heap(self, node, value=0) -> None:
        """
        Recursion print in console all heap node
        :param node: Node
        :param value: value
        :return: None
        """
        indent = "\t" * value
        print(f"{indent}Value: {node.value}")
        if node.right is not None:
            self._show_heap(node.right, value=value + 1)
        if node.left is not None:
            self._show_heap(node.left, value=value + 1)

    def list(self) -> None or list:
        """
        Convert heap in to list
        :return: List or None if heap is empty
        """
        if self.root is None:
            return None
        else:
            heap_list = []
            self._list(heap_list, [self.root])
            return heap_list

    def _list(self, heap_list: list, query) -> None:
        """
        Recursion convert heap in to list
        Add all elements by level in heap in to heap_list
        :return: None
        """
        if not query:
            return
        next_query = []
        for element in query:
            heap_list.append(element.value)
            if element.right is not None:
                next_query.append(element.right)
            if element.left is not None:
                next_query.append(element.left)

        if next_query:
            self._list(heap_list, next_query)

    def delete(self) -> None:
        """
        Delete all heap
        :return:
        """

        self.root = None

    def find(self, value) -> bool:
        """
        Find element in heap
        :param value: value
        :return: True -> if value in heap, False -> if value not in heap
        """
        if self.root is None:
            return False
        else:
            return self._find(value, self.root)

    def _find(self, value: int, node: Node) -> bool:
        """
        Recursion find element in heap
        :param value: value
        :param node: Node
        :return: True -> if value in heap, False -> if value not in heap
        """
        if value == node.value:
            return True
        res_left, res_right = False, False
        if node.left is not None:
            res_left = self._find(value, node.left)
        if node.right is not None:
            res_right = self._find(value, node.right)

        return bool(res_left + res_right)

    def show_max(self) -> None or int:
        """
        Return MAX value in heap
        :return:
        """

        if self.root is not None:
            return self.root.value
        else:
            return None

if __name__ == "__main__":
    heap = Heap()
    for _ in range(10):
        add_value = random.randint(1, 10)
        heap.add(add_value)
    heap.add(2)
    heap.show_heap()
    print(f"Find value 9 result: {heap.find(9)}")
    print(f"Convert heap to list: {heap.list()}")
    print(f"Max value in heap: {heap.show_max()}")
