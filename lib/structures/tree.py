from abc import ABC, abstractmethod
from typing import cast
from collections import deque
from enum import Enum, unique

from structures.node import _BaseNode, BinaryNode, GeneralNode


@unique
class BtInsertionMethod(Enum):
    BST_INSERT = 0
    COMPLETE_INSERT = 1
    LEFT_INSERT = 2
    RIGHT_INSERT = 3


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
    def insert(self, node: _BaseNode, insertion: Enum) -> None:
        raise NotImplementedError("Cannot call method of abstract class")


class GeneralTree(_BaseTree):
    def __init__(
        self,
        root: GeneralNode
    ) -> None:
        root.check_type(root, GeneralNode)
        super().__init__(root)

    @property
    def root(self) -> _BaseNode:
        return self._root

    @root.setter
    def root(self, root: _BaseNode) -> None:
        root.check_type(root, GeneralNode)
        self._root = root

    # TODO: Compelete general tree insertion techniques
    def insert(self, node: _BaseNode, _: Enum) -> None:
        node.check_type(node, GeneralNode)
        if not self.root:
            self.root = node
            return

        raise NotImplementedError("GeneralTree insertion not implemented")


class BinaryTree(_BaseTree):
    def __init__(
        self,
        root: BinaryNode
    ) -> None:
        root.check_type(root, BinaryNode)
        super().__init__(root)

    @property
    def root(self) -> _BaseNode:
        return self._root

    @root.setter
    def root(self, root: _BaseNode) -> None:
        root.check_type(root, BinaryNode)
        self._root = root

    def insert(
        self,
        node: _BaseNode,
        insertion: Enum
    ) -> None:
        node.check_type(node, BinaryNode)
        node = cast(BinaryNode, node)
        if not self.root:
            self.root = node
            return

        match insertion:
            case BtInsertionMethod.BST_INSERT:
                self._bst_insert(node, cast(BinaryNode, self.root))
            case BtInsertionMethod.COMPLETE_INSERT:
                self._complete_bt_insert(node)
            case BtInsertionMethod.LEFT_INSERT:
                self._left_insert(node)
            case BtInsertionMethod.RIGHT_INSERT:
                self._right_insert(node)
            case _:
                raise ValueError(f"Insertion options do not include {insertion}")

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
