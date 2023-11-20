from __future__ import annotations
from typing import List, Any, Optional


class Node:
    def __init__(self) -> None:
        self._parent: Node = Node()
        self._children: List[Node] = []
        self._data: Optional[Any] = None

    @property
    def parent(self) -> Node:
        return self._parent

    @parent.setter
    def parent(self, parent: Node) -> None:
        self._parent = parent

    @property
    def children(self) -> List[Node]:
        return self._children

    @property
    def data(self) -> Optional[Any]:
        return self._data

    @data.setter
    def data(self, data: Any) -> None:
        self._data = data

    def add_child(self, child: Node) -> None:
        self._children.append(child)
