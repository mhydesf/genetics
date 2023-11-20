from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, List, Optional, Type, TypeVar


T = TypeVar("T")


class _BaseNode(ABC, Generic[T]):
    def __init__(
        self,
        data: T,
        parent: Optional[_BaseNode] = None,
    ) -> None:
        self.data = data
        self._parent = parent

    @property
    @abstractmethod
    def parent(self) -> Optional[_BaseNode]:
        raise NotImplementedError("Cannot call method of abstract class")

    @parent.setter
    @abstractmethod
    def parent(self, parent: _BaseNode) -> _BaseNode:
        raise NotImplementedError("Cannot call method of abstract class")

    @property
    @abstractmethod
    def data(self) -> T:
        raise NotImplementedError("Cannot call method of abstract class")

    @data.setter
    @abstractmethod
    def data(self, data: T) -> None:
        raise NotImplementedError("Cannot call method of abstract class")

    @staticmethod
    def check_type(
        node: _BaseNode,
        node_type: Type[_BaseNode]
    ) -> None:
        if not isinstance(node, GeneralNode):
            raise TypeError(
                f"Node is of type {type(node)} but should by of type {node_type}"
            )


class GeneralNode(_BaseNode[T]):
    def __init__(
        self,
        data: T,
        parent: Optional[_BaseNode] = None,
    ) -> None:
        if parent:
            self.check_type(parent, GeneralNode)
        super().__init__(data, parent)
        self._children: List[_BaseNode] = []

    @property
    def parent(self) -> Optional[_BaseNode]:
        return self._parent

    @parent.setter
    def parent(self, parent: _BaseNode) -> None:
        self.check_type(parent, GeneralNode)
        self._parent = parent

    @property
    def data(self) -> T:
        return self._data

    @data.setter
    def data(self, data: T) -> None:
        self._data = data

    @property
    def children(self) -> List[_BaseNode]:
        return self._children

    def add_child(self, child: _BaseNode) -> None:
        self.check_type(child, GeneralNode)
        self._children.append(child)


class BinaryNode(_BaseNode[T]):
    def __init__(
        self,
        data: T,
        parent: Optional[_BaseNode] = None,
    ) -> None:
        if parent:
            self.check_type(parent, BinaryNode)
        super().__init__(data, parent)
        self._left_child: Optional[BinaryNode] = None
        self._right_child: Optional[BinaryNode] = None

    @property
    def parent(self) -> Optional[_BaseNode]:
        return self._parent

    @parent.setter
    def parent(self, parent: _BaseNode) -> None:
        self.check_type(parent, BinaryNode)
        self._parent = parent

    @property
    def data(self) -> T:
        return self._data

    @data.setter
    def data(self, data: T) -> None:
        self._data = data

    @property
    def left_child(self) -> Optional[BinaryNode]:
        return self._left_child

    @left_child.setter
    def left_child(self, child: BinaryNode) -> None:
        self.check_type(child, BinaryNode)
        self._left_child = child

    @property
    def right_child(self) -> Optional[BinaryNode]:
        return self._right_child

    @right_child.setter
    def right_child(self, child: BinaryNode) -> None:
        self.check_type(child, BinaryNode)
        self._right_child = child
