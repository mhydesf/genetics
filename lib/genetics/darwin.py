from collections import Counter
import random
from typing import Dict, Tuple, List, Callable, Any
from genetics.population import Population

from structures.solution_node import SolutionNode, T
from structures.solution_tree import SolutionTree


class Darwin:
    @staticmethod
    def crossover(
        tree1: SolutionTree,
        tree2: SolutionTree,
    ) -> Tuple[SolutionTree, SolutionTree]:
        point1 = Darwin._select_prune_node(tree1.root)
        point2 = Darwin._select_prune_node(tree2.root)
        Darwin._swap_subtrees(point1, point2)

        return tree1, tree2

    # TODO: This method results in ever growing tree depth.
    # That's a no-go
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

    # TODO: This should preserve the original population
    # size
    @staticmethod
    def tournament_selection(population: Dict[SolutionTree, float]) -> Population:
        items = list(population.items())
        random.shuffle(items)

        selected = []
        for i in range(0, len(items), 2):
            if i + 1 < len(items):
                item1 = items[i]
                item2 = items[i + 1]
                selected.append(max(item1, item2, key=lambda x: x[1])[0])

        return selected

    @staticmethod
    def next_generation(fittest: List[SolutionTree], size: int):
        random.shuffle(fittest)
        children = []
        for mother, father in zip(fittest[::2], fittest[1::2]):
            daughter, son = Darwin.crossover(mother, father)
            children.append(daughter)
            children.append(son)
        next_gen = children + fittest
        random.shuffle(next_gen)
        return next_gen[:size]

    # TODO: This is a hack solution - need to find a better way
    # to handle duplication
    @staticmethod
    def mutate_duplicates(
        solutions: List[SolutionTree],
        operators: List[Callable[..., Any]],
        operands: List[T],
        max_depth: int,
    ) -> List[SolutionTree]:
        duplicates = Darwin._find_duplicates(solutions)
        for idx, solution in enumerate(solutions):
            if solution in duplicates:
                root = SolutionTree.generate_random_tree(
                    operators,
                    operands,
                    max_depth
                )
                solutions[idx] = SolutionTree(root)
        return solutions

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

    # TODO: See Darwin.mutate_duplicates
    @staticmethod
    def _find_duplicates(solutions: List[SolutionTree]) -> List[SolutionTree]:
        counts = Counter(solutions)
        return [solution for solution, count in counts.items() if count > 1]
