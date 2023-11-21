from __future__ import annotations
import inspect
from math import inf
from typing import (
    Any,
    Callable,
    Dict,
    Optional,
    SupportsFloat,
    SupportsInt,
    TypeVar,
    Union,
    cast,
)


T = TypeVar("T", bound=Union[Callable, SupportsInt, SupportsFloat])


class SolutionNode:
    def __init__(
        self,
        data: T,
        parent: Optional[SolutionNode] = None,
    ) -> None:
        if parent:
            self.check_type(parent)
        self._parent = parent
        self._data = data
        self._left_child: Optional[SolutionNode] = None
        self._right_child: Optional[SolutionNode] = None

    def __repr__(self):
        return f"{self.data.__name__ if callable(self.data) else self.data}"

    @staticmethod
    def check_type(node: SolutionNode) -> None:
        if not isinstance(node, SolutionNode):
            raise TypeError(
                f"Node is of type {type(node)} but should by of type {SolutionNode}"
            )

    @property
    def parent(self) -> Optional[SolutionNode]:
        return self._parent

    @parent.setter
    def parent(self, parent: SolutionNode) -> None:
        self.check_type(parent)
        self._parent = parent

    @property
    def data(self) -> Callable[..., Any] | SupportsInt | SupportsFloat:
        return self._data

    @data.setter
    def data(self, data: T) -> None:
        self._data = data

    @property
    def left_child(self) -> Optional[SolutionNode]:
        return self._left_child

    @left_child.setter
    def left_child(self, child: SolutionNode) -> None:
        self.check_type(child)
        self._left_child = child

    @property
    def right_child(self) -> Optional[SolutionNode]:
        return self._right_child

    @right_child.setter
    def right_child(self, child: SolutionNode) -> None:
        self.check_type(child)
        self._right_child = child

    def evaluate(
        self, context: Dict[str, T]
    ) -> Callable[..., Any] | SupportsInt | SupportsFloat:
        if callable(self.data):
            sig = inspect.signature(self.data)
            num_args = len(sig.parameters)
            left_result = self.left_child.evaluate(context) if self.left_child else None
            if num_args > 1:
                right_result = (
                    self.right_child.evaluate(context) if self.right_child else None
                )
                try:
                    return self.data(left_result, right_result)
                except ZeroDivisionError:
                    return cast(T, inf)
            return self.data(left_result)
        if isinstance(self.data, str):
            return context[self.data]
        return self.data
