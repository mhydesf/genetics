from abc import ABC, abstractmethod
from typing import cast
from collections import deque

from structures.node import _BaseNode, BinaryNode, GeneralNode


class _BaseTree(ABC):
    def __init__(
        self,
        root: _BaseNode
    ) -> None:
        self._root = root

    @property
    @abstractmethod
    def root(self) -> _BaseNode:
        raise NotImplementedError("Cannot call method of abstract class")

    @root.setter
    @abstractmethod
    def root(self, root: _BaseNode) -> None:
        raise NotImplementedError("Cannot call method of abstract class")

    @abstractmethod
    def insert(self, node: _BaseNode) -> None:
        raise NotImplementedError("Cannot call method of abstract class")


class Tree(_BaseTree):
    def __init__(
        self,
        root: GeneralNode
    ) -> None:
        if root:
            root.check_type(root, GeneralNode)
        super().__init__(root)

    @property
    def root(self) -> _BaseNode:
        return self._root

    @root.setter
    def root(self, root: _BaseNode) -> None:
        root.check_type(root, GeneralNode)
        self._root = root

    def insert(self, node: _BaseNode) -> None:
        node.check_type(node, GeneralNode)
        if not self.root:
            self.root = node
            return


class BinaryTree(_BaseTree):
    def __init__(
        self,
        root: BinaryNode
    ) -> None:
        if root:
            root.check_type(root, BinaryNode)
        super().__init__(root)

    @property
    def root(self) -> _BaseNode:
        return self._root

    @root.setter
    def root(self, root: _BaseNode) -> None:
        root.check_type(root, BinaryNode)
        self._root = root

    def insert(self, node: _BaseNode) -> None:
        node.check_type(node, BinaryNode)
        if not self.root:
            self.root = node
            return

    def _bst_insert(
        self,
        node: BinaryNode,
        current: BinaryNode
    ) -> None:
        if node.data < current.data:
            if current.left_child is None:
                current.left_child = node
            else:
                self._bst_insert(node, current.left_child)
        else:
            if current.right_child is None:
                current.right_child = node
            else:
                self._bst_insert(node, current.right_child)

    def _complete_bt_insert(self, node: BinaryNode) -> None:
        queue = deque([self.root])
        while queue:
            current = cast(BinaryNode, queue.popleft())
            if not current.left_child:
                current.left_child = node
                return
            queue.append(current.left_child)
            if not current.right_child:
                current.right_child = node
                return
            queue.append(current.right_child)

    def _left_insert(self, node: BinaryNode) -> None:
        queue = deque([self.root])
        while queue:
            current = cast(BinaryNode, queue.popleft())
            if not current.left_child:
                current.left_child = node
                return
            queue.append(current.left_child)

    def _right_insert(self, node: BinaryNode) -> None:
        queue = deque([self.root])
        while queue:
            current = cast(BinaryNode, queue.popleft())
            if not current.right_child:
                current.right_child = node
                return
            queue.append(current.right_child)
