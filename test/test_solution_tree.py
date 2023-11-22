import operator
from unittest import TestCase, main
from structures.solution_node import SolutionNode
from structures.solution_tree import SolutionTree


class TestSolutionTree(TestCase):
    def test_tree_creation(self):
        root = SolutionNode(1)
        tree = SolutionTree(root)
        self.assertEqual(tree.root, root)

    def test_set_root(self):
        root = SolutionNode(1)
        new_root = SolutionNode(10)
        tree = SolutionTree(root)
        tree.root = new_root
        self.assertEqual(tree.root, new_root)

    def test_add_wrong_type(self):
        root = int(1)
        with self.assertRaises(TypeError):
            _ = SolutionTree(root)

    def test_evaluate(self):
        tree = SolutionTree(SolutionNode(operator.add))
        tree.root.left_child = SolutionNode(operator.mul)
        tree.root.left_child.left_child = SolutionNode(3)
        tree.root.left_child.right_child = SolutionNode(4)
        tree.root.right_child = SolutionNode(operator.mul)
        tree.root.right_child.left_child = SolutionNode(1)
        tree.root.right_child.right_child = SolutionNode(2)
        self.assertEqual(tree.evaluate({}), 14)


if __name__ == "__main__":
    main()
