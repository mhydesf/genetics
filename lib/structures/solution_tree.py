from __future__ import annotations
import random
import inspect
import operator
import math
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    SupportsFloat,
    SupportsInt,
    cast,
)

from structures.solution_node import T, SolutionNode


SYMBOLS = {
    operator.add: "+",
    operator.sub: "-",
    operator.mul: "*",
    operator.truediv: "/",
    math.exp: "exp",
    math.pow: "pow",
    math.log: "ln",
    math.sin: "sin",
    math.cos: "cos",
    math.tan: "tan",
    math.sinh: "sinh",
    math.cosh: "cosh",
    math.tanh: "tanh",
}


class SolutionTree:
    def __init__(self, root: SolutionNode) -> None:
        if not isinstance(root, SolutionNode):
            raise TypeError(f"Invalid type {type(root)} expected {SolutionNode}")
        self._root = root

    def __repr__(self) -> str:
        return self.print_equation(self.root)

    @property
    def root(self) -> SolutionNode:
        return self._root

    @root.setter
    def root(self, node: SolutionNode) -> None:
        if not isinstance(node, SolutionNode):
            raise TypeError
        self._root = node

    def evaluate(
        self, context: Dict[str, T]
    ) -> Callable[..., Any] | SupportsInt | SupportsFloat:
        return self.root.evaluate(context)

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
        self, node: SolutionNode, indent: str = "", side: str = "root"
    ) -> None:
        if node is not None:
            self._print_node(node, indent, side)

            left_indent = self._update_indent(indent, side)
            right_indent = self._update_indent(indent, side)

            if node.left_child:
                self.print_tree(node.left_child, left_indent, side="left")
            if node.right_child:
                self.print_tree(node.right_child, right_indent, side="right")

    def print_equation(self, node: SolutionNode) -> str:
        if node is None:
            return ""

        equation = self._generate_equation(node)
        return f"f = {equation}"

    def _print_node(self, node: SolutionNode, indent: str, side: str) -> None:
        branch = "└── " if side == "right" else "┌── "
        if side == "root":
            print(node)
            return
        print(f"{indent}{branch}{node}")

    def _update_indent(self, indent: str, side: str) -> str:
        if side == "root":
            return indent
        if side == "left":
            return indent + "│   "
        return indent + "    "

    def _generate_equation(self, node: SolutionNode) -> str:
        if callable(node.data):
            left_side = (
                self._generate_equation(node.left_child) if node.left_child else ""
            )
            right_side = (
                self._generate_equation(node.right_child) if node.right_child else ""
            )
            operator_symbol = SYMBOLS.get(node.data, "?")
            equation = (
                f"{left_side} {operator_symbol} {right_side}"
                if right_side
                else f"{operator_symbol}({left_side})"
            )
            return f"({equation})" if node.left_child else equation
        return str(node.data)
