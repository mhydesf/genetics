import operator
import numpy as np
from statistics import mean

from genetics.darwin import Darwin
from genetics.population import Population
from structures.solution_tree import SolutionTree, math


def linear(x: int, a: int = 1):
    return a*x


def quadratic(x: int, a: int = 1):
    return a*x**2


def minimize_difference(solution: SolutionTree) -> float:
    diff = []
    for i in np.linspace(1,10,10):
        diff.append(abs(quadratic(i) - solution.evaluate(context={'x': i})))
    return mean(diff)


def main():
    SIZE = 100
    OPERATORS = [
        operator.add,
        operator.sub,
        operator.mul,
        operator.truediv,
        math.pow,
    ]
    consts = [x for x in range(100)]
    vars = ['x']
    OPERANDS = consts + vars
    MAX_DEPTH = 3

    population = Population.generate_population(
        size=SIZE,
        operators=OPERATORS,
        operands=OPERANDS,
        max_depth=MAX_DEPTH
    )

    population.fitness = minimize_difference
    for i in range(1000):
        fit = population.evaluate_fitness()
        fittest = Darwin.tournament_selection(fit)
        next_gen = Darwin.next_generation(fittest, population.size)
        next_gen = Darwin.mutate_duplicates(
            next_gen,
            OPERATORS,
            OPERANDS,
            1
        )
        population.solutions = next_gen
        if min(fit.values()) <= 0.05:
            print(f"Result is {min(fit, key=fit.get)} with a fitness score of {min(fit.values())} after {i} iterations")
            break
        print(min(fit.values()))


if __name__ == "__main__":
    main()
