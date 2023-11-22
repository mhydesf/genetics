import operator
from unittest import TestCase, main
from structures.solution_node import SolutionNode


class TestSolutionNode(TestCase):
    def test_binary_node_creation(self):
        node = SolutionNode(10)
        self.assertEqual(node.data, 10)
        self.assertIsNone(node.parent)
        self.assertIsNone(node.left_child)
        self.assertIsNone(node.right_child)

    def test_set_left_right_child(self):
        parent = SolutionNode(1)
        left_child = SolutionNode(2)
        right_child = SolutionNode(3)
        parent.left_child = left_child
        parent.right_child = right_child
        self.assertEqual(parent.left_child, left_child)
        self.assertEqual(parent.right_child, right_child)
        with self.assertRaises(TypeError):
            left_child.left_child = 1
        with self.assertRaises(TypeError):
            right_child.right_child = 1

    def test_set_parent(self):
        parent = SolutionNode(1)
        child = SolutionNode(2)
        child.parent = parent
        self.assertEqual(child.parent, parent)
        with self.assertRaises(TypeError):
            parent.parent = 1

    def test_set_data(self):
        node = SolutionNode(1)
        node.data = 3
        self.assertEqual(node.data, 3)

    def test_evaluate(self):
        node = SolutionNode(operator.add)
        node.left_child = SolutionNode(1)
        node.right_child = SolutionNode(1)
        self.assertEqual(node.evaluate({}), 2)


if __name__ == "__main__":
    main()
