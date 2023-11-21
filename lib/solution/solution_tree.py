from __future__ import annotations
import inspect
from typing import Callable, Dict, List, Optional, cast
from math import cos
import operator
import random

from structures.node import T, BinaryNode
from structures.tree import BinaryTree
from solution.solution_node import SolutionNode


SYMBOLS = {
    operator.add: '+',
    operator.sub: '-',
    operator.mul: '*',
    operator.truediv: '/',
    cos: 'cos'
}


class SolutionTree(BinaryTree):
    def __init__(
        self,
        root: SolutionNode
    ) -> None:
        self._root = root
        super().__init__(cast(BinaryNode, self._root))

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
        sig = inspect.signature(operator_func)
        num_args = len(sig.parameters)

        node.left_child = SolutionTree.generate_random_tree(
            operators, operands, max_depth, current_depth + 1, node
        )
        if num_args > 1:
            node.right_child = SolutionTree.generate_random_tree(
                operators, operands, max_depth, current_depth + 1, node
            )

        return node

    def print_tree(
        self,
        node: SolutionNode,
        indent: str = "",
        side: str = "root"
    ) -> None:
        if node is not None:
            if side == "root":
                print(node)
            else:
                branch = ("└── " if side == "right" else "┌── ")
                print(f"{indent}{branch}{node}")

            if side == "root":
                next_indent = indent
            elif side == "left":
                next_indent = indent + "│   "
            else:
                next_indent = indent + "    "

            if node.left_child:
                self.print_tree(node.left_child, next_indent, side="left")
            if node.right_child:
                self.print_tree(node.right_child, next_indent, side="right")

    def print_equation(
        self,
        node: SolutionNode,
        is_root: bool = True
    ) -> str:
        if node is None:
            return ""

        if callable(node.data):
            if node.left_child:
                left_side = self.print_equation(node.left_child, False)
            else:
                left_side = ""
            if node.right_child:
                right_side = self.print_equation(node.right_child, False)
            else:
                right_side = ""
            operator_symbol = SYMBOLS.get(node.data, '?')

            if is_root:
                return f"f = {left_side} {operator_symbol} {right_side}"
            return f"({left_side} {operator_symbol} {right_side})"

        return str(node.data)
