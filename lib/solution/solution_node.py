from __future__ import annotations
from typing import Optional, cast
from structures.node import T, NodeT, SupportsComparators, BinaryNode


class SolutionNode(BinaryNode[T, NodeT]):
    def __init__(
        self,
        data: T,
        parent: Optional[NodeT] = None,
    ) -> None:
        if parent:
            self.check_type(parent, SolutionNode)
        super().__init__(data, parent)
        self._left_child: Optional[NodeT] = None
        self._right_child: Optional[NodeT] = None

    def __repr__(self):
        return f"{self.data.__name__ if callable(self.data) else self.data}"

    @property
    def parent(self) -> Optional[NodeT]:
        return self._parent

    @parent.setter
    def parent(self, parent: NodeT) -> None:
        self.check_type(parent, SolutionNode)
        self._parent = parent

    @property
    def left_child(self) -> Optional[NodeT]:
        return self._left_child

    @left_child.setter
    def left_child(self, child: NodeT) -> None:
        self.check_type(child, SolutionNode)
        self._left_child = child

    @property
    def right_child(self) -> Optional[NodeT]:
        return self._right_child

    @right_child.setter
    def right_child(self, child: NodeT) -> None:
        self.check_type(child, SolutionNode)
        self._right_child = child

    def evaluate(self) -> SupportsComparators:
        if callable(self.data):
            left_result = (
                cast(SolutionNode, self.left_child).evaluate()
                if self.left_child
                else None
            )
            right_result = (
                cast(SolutionNode, self.right_child).evaluate()
                if self.right_child
                else None
            )
            return self.data(left_result, right_result)
        return self.data
