import operator
from unittest import TestCase, main
from solution.solution_node import SolutionNode
from solution.solution_tree import SolutionTree


class TestSolutionTree(TestCase):
    def test_evaluate(self):
        tree = SolutionTree(SolutionNode(operator.add))
        tree.root.left_child = SolutionNode(operator.mul)
        tree.root.left_child.left_child = SolutionNode(3)
        tree.root.left_child.right_child = SolutionNode(4)
        tree.root.right_child = SolutionNode(operator.mul)
        tree.root.right_child.left_child = SolutionNode(1)
        tree.root.right_child.right_child = SolutionNode(2)
        self.assertEqual(tree.evaluate(), 14)


if __name__ == "__main__":
    main()
