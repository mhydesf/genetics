import operator
from solution.solution_tree import SolutionTree
from math import cos

operators = [cos, operator.add, operator.sub, operator.mul, operator.truediv]
operands = [1, 2, 'x', 'y']
max_depth = 3

root_node = SolutionTree.generate_random_tree(operators, operands, max_depth)
solution_tree = SolutionTree(root_node)

context = {'x': 5, 'y': 10}
print(f"Context: {context}")
print(f"Solution: {solution_tree.evaluate(context)}")
solution_tree.print_tree(solution_tree.root)
print(f"Function: {solution_tree}")
