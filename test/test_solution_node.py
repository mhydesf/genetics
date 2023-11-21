import operator
from unittest import TestCase, main
from structures.solution_node import SolutionNode


class TestSolutionNode(TestCase):
    def test_evaluate(self):
        node = SolutionNode(operator.add)
        node.left_child = SolutionNode(1)
        node.right_child = SolutionNode(1)
        self.assertEqual(node.evaluate({}), 2)


if __name__ == "__main__":
    main()
