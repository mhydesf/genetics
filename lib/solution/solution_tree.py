from __future__ import annotations
from typing import Callable, List, cast

from structures.node import T, BinaryNode
from structures.tree import BinaryTree
from solution.solution_node import SolutionNode


class SolutionTree(BinaryTree):
    def __init__(
        self,
        root: SolutionNode
    ) -> None:
        self._root = root
        super().__init__(cast(BinaryNode, self._root))

    # TODO: Implement this
    @staticmethod
    def generate_random_tree(
        operators: List[Callable],
        operands: List[T],
        max_depth: int,
        current_depth: int = 0) -> SolutionTree:
        print(operators)
        print(operands)
        print(max_depth)
        print(current_depth)
        return SolutionTree(SolutionNode(1))

    def evaluate(self) -> T:
        return cast(SolutionNode, self.root).evaluate()
