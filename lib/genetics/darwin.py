import random
from typing import Tuple, List, Callable, Any

from structures.solution_node import SolutionNode, T
from structures.solution_tree import SolutionTree


class Darwin:
    def __init__(self) -> None:
        pass

    @staticmethod
    def crossover(
        tree1: SolutionTree,
        tree2: SolutionTree,
    ) -> Tuple[SolutionTree, SolutionTree]:
        point1 = Darwin._select_prune_node(tree1.root)
        point2 = Darwin._select_prune_node(tree2.root)

        Darwin._swap_subtrees(point1, point2)

        return tree1, tree2

    @staticmethod
    def mutation(
        tree: SolutionTree,
        operators: List[Callable[..., Any]],
        operands: List[T],
        max_depth: int,
    ) -> SolutionTree:
        node = Darwin._select_prune_node(tree.root)
        parent = node.parent
        node.parent = None
        root = SolutionTree.generate_random_tree(
            operators=operators,
            operands=operands,
            max_depth=max_depth,
        )
        if parent:
            if parent.left_child == node:
                parent.left_child = root
            elif parent.right_child == node:
                parent.right_child = root
        else:
            tree.root = root
        root.parent = parent
        return SolutionTree(tree.root)

    @staticmethod
    def _select_prune_node(node: SolutionNode) -> SolutionNode:
        current = node
        while current.left_child or current.right_child:
            possible_next_nodes = []
            if current.left_child:
                possible_next_nodes.append(current.left_child)
            if current.right_child:
                possible_next_nodes.append(current.right_child)
            if possible_next_nodes:
                current = random.choice(possible_next_nodes)
            else:
                break
        return current

    @staticmethod
    def _swap_subtrees(
        node1: SolutionNode,
        node2: SolutionNode
    ) -> None:
        if node1.parent and node2.parent:
            if node1.parent.left_child == node1:
                node1.parent.left_child = node2
            else:
                node1.parent.right_child = node2
            if node2.parent.left_child == node2:
                node2.parent.left_child = node1
            else:
                node2.parent.right_child = node1
            node1.parent, node2.parent = node2.parent, node1.parent
        else:
            raise ValueError("Both nodes must have parents for the swap to work")
