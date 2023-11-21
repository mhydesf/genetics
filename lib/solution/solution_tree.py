from __future__ import annotations
from typing import Callable, List, cast
from typing import Callable, Dict, List, Optional, cast
import operator
import random

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
    def __repr__(self) -> str:
        return self.print_equation(cast(SolutionNode, self.root), True)

    def evaluate(self, context: Dict[str, T]) -> T:
        return cast(SolutionNode, self.root).evaluate(context)

    @staticmethod
    def generate_random_tree(
        operators: List[Callable],
        operands: List[T],
        max_depth: int,
        current_depth: int = 0,
        parent: Optional[SolutionNode] = None,
    ) -> SolutionNode:
        if current_depth >= max_depth or (current_depth > 0 and random.random() > 0.5):
            terminal_value = random.choice(operands)
            return SolutionNode(terminal_value, parent)

        operator_func = random.choice(operators)
        node = SolutionNode(cast(T, operator_func), parent)

        node.left_child = SolutionTree.generate_random_tree(
            operators, operands, max_depth, current_depth + 1, node
        )
        node.right_child = SolutionTree.generate_random_tree(
            operators, operands, max_depth, current_depth + 1, node
        )

        return node
