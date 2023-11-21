from unittest import TestCase, main
from structures.node import GeneralNode, BinaryNode

class NonComparatorClass:
    def __init__(self, data: int) -> None:
        self.data: int = data

class TestGeneralNode(TestCase):
    def test_node_creation(self):
        node = GeneralNode(5)
        self.assertEqual(node.data, 5)
        self.assertIsNone(node.parent)
        self.assertEqual(node.children, [])

    def test_add_child(self):
        parent = GeneralNode(1)
        child = GeneralNode(2)
        parent.add_child(child)
        self.assertIn(child, parent.children)

    def test_set_parent(self):
        parent = GeneralNode(1)
        child = GeneralNode(2)
        child.parent = parent
        self.assertEqual(child.parent, parent)

    def test_set_data(self):
        node = GeneralNode(1)
        node.data = 3
        self.assertEqual(node.data, 3)

    def test_equals(self):
        left_node = GeneralNode(1)
        right_node = GeneralNode(1)
        self.assertEqual(left_node, right_node)

    def test_not_equals(self):
        left_node = GeneralNode(1)
        right_node = GeneralNode(2)
        self.assertNotEqual(left_node, right_node)

    def test_less_than(self):
        left_node = GeneralNode(1)
        right_node = GeneralNode(2)
        self.assertLess(left_node, right_node)

    def test_less_than_equal(self):
        left_node = GeneralNode(1)
        right_node = GeneralNode(2)
        self.assertLessEqual(left_node, right_node)
        left_node = GeneralNode(2)
        self.assertLessEqual(left_node, right_node)

    def test_greater_than(self):
        left_node = GeneralNode(5)
        right_node = GeneralNode(2)
        self.assertGreater(left_node, right_node)

    def test_greater_than_equal(self):
        left_node = GeneralNode(5)
        right_node = GeneralNode(2)
        self.assertGreaterEqual(left_node, right_node)
        left_node = GeneralNode(2)
        self.assertGreaterEqual(left_node, right_node)

    def test_non_comparator_type(self):
        left_node = GeneralNode(NonComparatorClass(5))
        right_node = GeneralNode(NonComparatorClass(8))
        with self.assertRaises(TypeError):
            _ = left_node == right_node
            _ = left_node != right_node
            _ = left_node < right_node
            _ = left_node <= right_node
            _ = left_node >= right_node
            _ = left_node > right_node


class TestBinaryNode(TestCase):
    def test_binary_node_creation(self):
        node = BinaryNode(10)
        self.assertEqual(node.data, 10)
        self.assertIsNone(node.parent)
        self.assertIsNone(node.left_child)
        self.assertIsNone(node.right_child)

    def test_set_left_right_child(self):
        parent = BinaryNode(1)
        left_child = BinaryNode(2)
        right_child = BinaryNode(3)
        parent.left_child = left_child
        parent.right_child = right_child
        self.assertEqual(parent.left_child, left_child)
        self.assertEqual(parent.right_child, right_child)

    def test_set_parent(self):
        parent = BinaryNode(1)
        child = BinaryNode(2)
        child.parent = parent
        self.assertEqual(child.parent, parent)

    def test_set_data(self):
        node = BinaryNode(1)
        node.data = 3
        self.assertEqual(node.data, 3)

    def test_equals(self):
        left_node = BinaryNode(1)
        right_node = BinaryNode(1)
        self.assertEqual(left_node, right_node)

    def test_not_equals(self):
        left_node = BinaryNode(1)
        right_node = BinaryNode(2)
        self.assertNotEqual(left_node, right_node)

    def test_less_than(self):
        left_node = BinaryNode(1)
        right_node = BinaryNode(2)
        self.assertLess(left_node, right_node)

    def test_less_than_equal(self):
        left_node = BinaryNode(1)
        right_node = BinaryNode(2)
        self.assertLessEqual(left_node, right_node)
        left_node = BinaryNode(2)
        self.assertLessEqual(left_node, right_node)

    def test_greater_than(self):
        left_node = BinaryNode(5)
        right_node = BinaryNode(2)
        self.assertGreater(left_node, right_node)

    def test_greater_than_equal(self):
        left_node = BinaryNode(5)
        right_node = BinaryNode(2)
        self.assertGreaterEqual(left_node, right_node)
        left_node = BinaryNode(2)
        self.assertGreaterEqual(left_node, right_node)

    def test_non_comparator_type(self):
        left_node = BinaryNode(NonComparatorClass(5))
        right_node = BinaryNode(NonComparatorClass(8))
        with self.assertRaises(TypeError):
            _ = left_node == right_node
            _ = left_node != right_node
            _ = left_node < right_node
            _ = left_node <= right_node
            _ = left_node >= right_node
            _ = left_node > right_node


if __name__ == '__main__':
    main()
