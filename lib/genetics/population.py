from __future__ import annotations
from typing import Any, Callable, Dict, List, SupportsFloat, SupportsInt
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
        self._fitness: Callable[..., Any]

    @property
    def size(self) -> int:
        return self._size

    @property
    def solutions(self) -> List[SolutionTree]:
        return self._solutions

    @solutions.setter
    def solutions(self, solutions: List[SolutionTree]) -> None:
        self._solutions = solutions
        self._size = len(solutions)

    # TODO: This probably doesn't belong here
    @property
    def fitness(self) -> Callable[..., Any]:
        return self._fitness

    # TODO: This probably doesn't belong here
    @fitness.setter
    def fitness(self, fitness: Callable[..., Any]) -> None:
        if not callable(fitness):
            raise TypeError("Fitness funciton must be callable")
        self._fitness = fitness

    # TODO: This probably doesn't belong here
    def evaluate_fitness(self) -> Dict[SolutionTree, SupportsInt | SupportsFloat]:
        if self.fitness is None:
            raise ValueError("Fitness function has not been set")
        return {solution: self.fitness(solution) for solution in self.solutions}

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
