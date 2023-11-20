from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, List, Optional, TypeVar, cast


T = TypeVar("T")


class _BaseNode(ABC, Generic[T]):
    @property
    @abstractmethod
    def parent(self) -> _BaseNode:
        raise NotImplementedError("Cannot call method of abstract class")

    @parent.setter
    @abstractmethod
    def parent(self, _: _BaseNode) -> _BaseNode:
        raise NotImplementedError("Cannot call method of abstract class")

    @property
    @abstractmethod
    def data(self) -> Optional[T]:
        raise NotImplementedError("Cannot call method of abstract class")

    @data.setter
    @abstractmethod
    def data(self, data: T) -> None:
        raise NotImplementedError("Cannot call method of abstract class")


class GeneralNode(_BaseNode[T]):
    def __init__(self) -> None:
        self._parent: _BaseNode = cast(_BaseNode, None)
        self._data: Optional[T] = None
        self._children: List[_BaseNode] = []

    @property
    def parent(self) -> _BaseNode:
        return self._parent

    @parent.setter
    def parent(self, parent: _BaseNode) -> None:
        self._parent = parent

    @property
    def data(self) -> Optional[T]:
        return self._data

    @data.setter
    def data(self, data: T) -> None:
        self._data = data

    @property
    def children(self) -> List[_BaseNode]:
        return self._children

    def add_child(self, child: _BaseNode) -> None:
        self._children.append(child)


class BinaryNode(_BaseNode[T]):
    def __init__(self) -> None:
        self._parent: _BaseNode = cast(_BaseNode, None)
        self._data: Optional[T] = None
        self._left_child: Optional[_BaseNode] = None
        self._right_child: Optional[_BaseNode] = None

    @property
    def parent(self) -> _BaseNode:
        return self._parent

    @parent.setter
    def parent(self, parent: _BaseNode) -> None:
        self._parent = parent

    @property
    def data(self) -> Optional[T]:
        return self._data

    @data.setter
    def data(self, data: T) -> None:
        self._data = data

    @property
    def left_child(self) -> _BaseNode:
        return cast(_BaseNode, self._left_child)

    @left_child.setter
    def left_child(self, child: _BaseNode) -> None:
        self._left_child = child

    @property
    def right_child(self) -> _BaseNode:
        return cast(_BaseNode, self._right_child)

    @right_child.setter
    def right_child(self, child: _BaseNode) -> None:
        self._right_child = child
