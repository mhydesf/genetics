from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Generic, List, Optional, Protocol, Type, TypeVar


T = TypeVar("T", bound='SupportsComparators')
NodeT = TypeVar("NodeT", bound='_BaseNode')


class SupportsComparators(Protocol):
    def __eq__(self, other: object) -> bool:
        ...

    def __ne__(self, other: object) -> bool:
        ...

    def __lt__(self, other: Any) -> bool:
        ...

    def __le__(self, other: Any) -> bool:
        ...

    def __gt__(self, other: Any) -> bool:
        ...

    def __ge__(self, other: Any) -> bool:
        ...

    def __call__(self, *args, **kwargs) -> Any:
        ...


class _BaseNode(ABC, Generic[T, NodeT]):
    def __init__(
        self,
        data: T,
        parent: Optional[NodeT] = None,
    ) -> None:
        self._data = data
        self._parent = parent

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        try:
            return self.data == other.data
        except TypeError:
            return NotImplemented

    def __ne__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        try:
            return self.data != other.data
        except TypeError:
            return NotImplemented

    def __lt__(self, other: _BaseNode) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        try:
            return self.data < other.data
        except TypeError:
            return NotImplemented

    def __le__(self, other: _BaseNode) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        try:
            return self.data <= other.data
        except TypeError:
            return NotImplemented

    def __gt__(self, other: _BaseNode) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        try:
            return self.data > other.data
        except TypeError:
            return NotImplemented

    def __ge__(self, other: _BaseNode) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        try:
            return self.data >= other.data
        except TypeError:
            return NotImplemented

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
    def check_type(node: _BaseNode, node_type: Type[_BaseNode]) -> None:
        if not isinstance(node, node_type):
            raise TypeError(
                f"Node is of type {type(node)} but should by of type {node_type}"
            )


class GeneralNode(_BaseNode[T, NodeT]):
    def __init__(
        self,
        data: T,
        parent: Optional[NodeT] = None,
    ) -> None:
        if parent:
            self.check_type(parent, GeneralNode)
        super().__init__(data, parent)
        self._children: List[_BaseNode] = []

    @property
    def parent(self) -> Optional[_BaseNode]:
        return self._parent

    @parent.setter
    def parent(self, parent: NodeT) -> None:
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


class BinaryNode(_BaseNode[T, NodeT]):
    def __init__(
        self,
        data: T,
        parent: Optional[NodeT] = None,
    ) -> None:
        if parent:
            self.check_type(parent, BinaryNode)
        super().__init__(data, parent)
        self._left_child: Optional[NodeT] = None
        self._right_child: Optional[NodeT] = None

    @property
    def parent(self) -> Optional[NodeT]:
        return self._parent

    @parent.setter
    def parent(self, parent: NodeT) -> None:
        self.check_type(parent, BinaryNode)
        self._parent = parent

    @property
    def data(self) -> T:
        return self._data

    @data.setter
    def data(self, data: T) -> None:
        self._data = data

    @property
    def left_child(self) -> Optional[NodeT]:
        return self._left_child

    @left_child.setter
    def left_child(self, child: NodeT) -> None:
        self.check_type(child, BinaryNode)
        self._left_child = child

    @property
    def right_child(self) -> Optional[NodeT]:
        return self._right_child

    @right_child.setter
    def right_child(self, child: NodeT) -> None:
        self.check_type(child, BinaryNode)
        self._right_child = child
