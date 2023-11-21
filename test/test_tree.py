from unittest import TestCase, main
from structures.node import GeneralNode, BinaryNode
from structures.tree import Tree, BinaryTree


class TestTree(TestCase):
    def test_tree_creation(self):
        root = GeneralNode(1)
        tree = Tree(root)
        self.assertEqual(tree.root, root)

    def test_set_root(self):
        root = GeneralNode(1)
        new_root = GeneralNode(10)
        tree = Tree(root)
        tree.root = new_root
        self.assertEqual(tree.root, new_root)

    def test_add_wrong_type(self):
        root = BinaryNode(1)
        with self.assertRaises(TypeError):
            _ = Tree(root)


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


if __name__ == "__main__":
    main()
