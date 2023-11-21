from __future__ import annotations
from typing import cast

from structures.node import BinaryNode
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
    def generate_tree() -> SolutionTree:
        return SolutionTree(SolutionNode(1))
