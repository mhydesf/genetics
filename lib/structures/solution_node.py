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
        if parent and not isinstance(parent, SolutionNode):
            raise TypeError(f"Invalid type {type(parent)} expected {SolutionNode}")
        self._parent = parent
        self._data = data
        self._left_child: Optional[SolutionNode] = None
        self._right_child: Optional[SolutionNode] = None

    def __repr__(self):
        return f"{self.data.__name__ if callable(self.data) else self.data}"

    @property
    def parent(self) -> Optional[SolutionNode]:
        return self._parent

    @parent.setter
    def parent(self, parent: Optional[SolutionNode]) -> None:
        if not isinstance(parent, Optional[SolutionNode]):
            raise TypeError(f"Invalid type {type(parent)} expected {SolutionNode}")
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
        if not isinstance(child, SolutionNode):
            raise TypeError(f"Invalid type {type(child)} expected {SolutionNode}")
        self._left_child = child

    @property
    def right_child(self) -> Optional[SolutionNode]:
        return self._right_child

    @right_child.setter
    def right_child(self, child: SolutionNode) -> None:
        if not isinstance(child, SolutionNode):
            raise TypeError(f"Invalid type {type(child)} expected {SolutionNode}")
        self._right_child = child

    def evaluate(
        self,
        context: Dict[str, T],
    ) -> Callable[..., Any] | SupportsInt | SupportsFloat:
        if callable(self.data):
            return self._evaluate_callable(context)
        if isinstance(self.data, str):
            return context[self.data]
        return self.data

    def _evaluate_callable(self, context: Dict[str, T]) -> Any:
        left_result = self._evaluate_child(self.left_child, context)
        right_result = (
            self._evaluate_child(self.right_child, context)
            if self._has_multiple_args()
            else None
        )

        try:
            return self._invoke_data_callable(left_result, right_result)
        except (ZeroDivisionError, OverflowError, ValueError):
            return cast(T, inf)

    def _evaluate_child(
        self,
        child: Optional[SolutionNode],
        context: Dict[str, T]
    ) -> Any:
        return child.evaluate(context) if child else None

    def _has_multiple_args(self) -> bool:
        sig = inspect.signature(cast(Callable[..., Any], self.data))
        return len(sig.parameters) > 1

    # TODO: Handle the runtime warning
    def _invoke_data_callable(
        self,
        left_result: T,
        right_result: T
    ) -> Any:
        try:
            return (
                cast(Callable[..., Any], self.data)(left_result, right_result)
                if right_result is not None
                else cast(Callable[..., Any], self.data)(left_result)
            )
        except ZeroDivisionError:
            return cast(T, inf)
