from unittest import TestCase, main
from structures.node import GeneralNode, BinaryNode
from structures.tree import GeneralTree, BinaryTree, BtInsertionMethod


class TestGeneralTree(TestCase):
    def test_tree_creation(self):
        root = GeneralNode(1)
        tree = GeneralTree(root)
        self.assertEqual(tree.root, root)

    def test_set_root(self):
        root = GeneralNode(1)
        new_root = GeneralNode(10)
        tree = GeneralTree(root)
        tree.root = new_root
        self.assertEqual(tree.root, new_root)

    def test_add_wrong_type(self):
        root = BinaryNode(1)
        with self.assertRaises(TypeError):
            _ = GeneralTree(root)


class TestBinaryTree(TestCase):
    def test_tree_creation(self):
        root = BinaryNode(1)
        tree = BinaryTree(root)
        self.assertEqual(tree.root, root)

    def test_set_root(self):
        root = BinaryNode(1)
        new_root = BinaryNode(10)
        tree = BinaryTree(root)
        tree.root = new_root
        self.assertEqual(tree.root, new_root)

    def test_add_wrong_type(self):
        root = GeneralNode(1)
        with self.assertRaises(TypeError):
            _ = BinaryTree(root)

    def test_bst_insert(self):
        root = BinaryNode(10)
        tree = BinaryTree(root)
        left_node = BinaryNode(5)
        right_node = BinaryNode(15)
        tree.insert(left_node, BtInsertionMethod.BST_INSERT)
        tree.insert(right_node, BtInsertionMethod.BST_INSERT)
        self.assertEqual(tree.root.left_child, left_node)
        self.assertEqual(tree.root.right_child, right_node)

    def test_complete_insert(self):
        root = BinaryNode(1)
        left_child = BinaryNode(2)
        right_child = BinaryNode(3)
        new_node = BinaryNode(4)
        tree = BinaryTree(root)
        tree.insert(left_child, BtInsertionMethod.COMPLETE_INSERT)
        tree.insert(right_child, BtInsertionMethod.COMPLETE_INSERT)
        tree.insert(new_node, BtInsertionMethod.COMPLETE_INSERT)
        self.assertEqual(tree.root.left_child, left_child)
        self.assertEqual(tree.root.right_child, right_child)
        self.assertEqual(tree.root.left_child.left_child, new_node)

    def test_left_insert(self):
        root = BinaryNode(1)
        left_child = BinaryNode(2)
        tree = BinaryTree(root)
        tree.insert(left_child, BtInsertionMethod.LEFT_INSERT)
        self.assertEqual(tree.root.left_child, left_child)

    def test_right_insert(self):
        root = BinaryNode(1)
        right_child = BinaryNode(2)
        tree = BinaryTree(root)
        tree.insert(right_child, BtInsertionMethod.RIGHT_INSERT)
        self.assertEqual(tree.root.right_child, right_child)


if __name__ == "__main__":
    main()
