import math
import operator
from statistics import mean

from genetics.population import Population
from genetics.darwin import Darwin


OPERATORS = [
    operator.add,
    operator.sub,
    operator.mul,
    operator.truediv,
    math.exp,
    math.pow,
]
OPERANDS = [1, 2, 3, 5, "x"]
MAX_DEPTH = 3


def fitness(solution):
    re = []
    for idx, val in enumerate(solution):
        re.append(idx - val)
    return mean(re)


def main():
    population = Population.generate_population(
        size=1000,
        operators=OPERATORS,
        operands=OPERANDS,
        max_depth=MAX_DEPTH,
    )

    for _ in range(100):
        results = []
        for func in population.solutions:
            data = []
            for i in range(101):
                context = {"x": i}
                data.append(func.evaluate(context))
            results.append(data)

        fit = [fitness(s) for s in results]


if __name__ == "__main__":
    main()
