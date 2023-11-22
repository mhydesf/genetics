import operator
import math

from structures.solution_tree import SolutionTree

operators = [
    operator.add,
    operator.sub,
    operator.mul,
    operator.truediv,
    math.exp,
    math.pow,
    math.sin,
    math.cos,
    math.tan,
]
operands = [1, 2, 3, 4, 5, 'x', 'y', 'z']
max_depth = 3

root_node = SolutionTree.generate_random_tree(operators, operands, max_depth)
solution_tree = SolutionTree(root_node)

context = {'x': 5, 'y': 10, 'z': 3}
print(f"Context: {context}")
print(f"Solution: {solution_tree.evaluate(context)}")
solution_tree.print_tree(solution_tree.root)
print(f"Function: {solution_tree}")
