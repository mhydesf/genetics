from __future__ import annotations
from typing import cast

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
    def generate_random_tree(max_depth: int, current_depth: int = 0) -> SolutionTree:
        return SolutionTree(SolutionNode(1))

    def evaluate(self) -> T:
        return cast(SolutionNode, self.root).evaluate()
