from __future__ import annotations
from typing import Any, Callable, List
from structures.solution_node import T
from structures.solution_tree import SolutionTree


class Population:
    def __init__(
        self,
        size: int,
        solutions: List[SolutionTree],
    ) -> None:
        self._size = size
        self._solutions: List[SolutionTree] = solutions

    @property
    def size(self) -> int:
        return self._size

    @property
    def solutions(self) -> List[SolutionTree]:
        return self._solutions

    @solutions.setter
    def solutions(self, solutions: List[SolutionTree]) -> None:
        self._solutions = solutions

    @staticmethod
    def generate_population(
        size: int,
        operators: List[Callable[..., Any]],
        operands: List[T],
        max_depth: int,
    ) -> Population:
        solutions = [
            SolutionTree(
                SolutionTree.generate_random_tree(
                    operators=operators,
                    operands=operands,
                    max_depth=max_depth,
                )
            )
            for _ in range(size)
        ]
        return Population(size, solutions)
