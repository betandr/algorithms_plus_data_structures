import unittest

from structures.binary_tree import BinaryTreeNode, BinaryTree

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self._binary_tree = BinaryTree()

    def test_node_returns_value(self):
        node = BinaryTreeNode(1)
        assert(node.value == 1)

    def test_node_children_have_correct_values(self):
        root = BinaryTreeNode(1)
        left_child = BinaryTreeNode(2)
        right_child = BinaryTreeNode(3)

        root.left = left_child
        root.right = right_child

        assert(root.left.value == 2)
        assert(root.right.value == 3)

    def test_greater_than(self):
        lesser_node = BinaryTreeNode(2)
        greater_node = BinaryTreeNode(3)
        assert(greater_node.is_greater_than(lesser_node))

    def test_add_to_empty_tree_adds_node_to_root(self):
        self._binary_tree.add(1)
        assert(self._binary_tree._root.value == 1)

    def test_add_less_value_to_tree_with_only_root(self):
        self._binary_tree.add(2)
        self._binary_tree.add(1)
        assert(self._binary_tree._root.value == 2)
        assert(self._binary_tree._root.left.value == 1)

    def test_add_greater_value_to_tree_with_only_root(self):
        self._binary_tree.add(1)
        self._binary_tree.add(2)
        assert(self._binary_tree._root.value == 1)
        assert(self._binary_tree._root.right.value == 2)

    def test_add_increments_tree_counter(self):
        self._binary_tree.add(1)
        self._binary_tree.add(2)
        self._binary_tree.add(3)
        self._binary_tree.add(4)
        assert(self._binary_tree._counter == 4)

    def test_add_balanced_series(self):
        self._binary_tree.add(4)
        self._binary_tree.add(2)
        self._binary_tree.add(6)
        self._binary_tree.add(1)
        self._binary_tree.add(3)
        self._binary_tree.add(5)
        self._binary_tree.add(7)
        root = self._binary_tree._root
        assert(root.value == 4)
        assert(root.left.value == 2)
        assert(root.right.value == 6)
        assert(root.left.left.value == 1)
        assert(root.left.right.value == 3)
        assert(root.right.left.value == 5)
        assert(root.right.right.value == 7)

    def test_add_left_unbalanced_series(self):
        self._binary_tree.add(7)
        self._binary_tree.add(6)
        self._binary_tree.add(5)
        self._binary_tree.add(4)
        self._binary_tree.add(3)
        self._binary_tree.add(2)
        self._binary_tree.add(1)
        root = self._binary_tree._root
        assert(root.value == 7)
        assert(root.left.value == 6)
        assert(root.left.left.value == 5)
        assert(root.left.left.left.value == 4)
        assert(root.left.left.left.left.value == 3)
        assert(root.left.left.left.left.left.value == 2)
        assert(root.left.left.left.left.left.left.value == 1)

    def test_add_right_unbalanced_series(self):
        self._binary_tree.add(1)
        self._binary_tree.add(2)
        self._binary_tree.add(3)
        self._binary_tree.add(4)
        self._binary_tree.add(5)
        self._binary_tree.add(6)
        self._binary_tree.add(7)
        root = self._binary_tree._root
        assert(root.value == 1)
        assert(root.right.value == 2)
        assert(root.right.right.value == 3)
        assert(root.right.right.right.value == 4)
        assert(root.right.right.right.right.value == 5)
        assert(root.right.right.right.right.right.value == 6)
        assert(root.right.right.right.right.right.right.value == 7)

    def test_contains_values_in_balanced_tree(self):
        self._binary_tree.add(4)
        self._binary_tree.add(2)
        self._binary_tree.add(6)
        self._binary_tree.add(1)
        self._binary_tree.add(3)
        self._binary_tree.add(5)
        self._binary_tree.add(7)
        assert(self._binary_tree.contains(1))
        assert(self._binary_tree.contains(2))
        assert(self._binary_tree.contains(3))
        assert(self._binary_tree.contains(4))
        assert(self._binary_tree.contains(5))
        assert(self._binary_tree.contains(6))
        assert(self._binary_tree.contains(7))
        self.assertFalse(self._binary_tree.contains(8))

    def test_contains_values_in_left_unbalanced_tree(self):
        self._binary_tree.add(7)
        self._binary_tree.add(6)
        self._binary_tree.add(5)
        self._binary_tree.add(4)
        self._binary_tree.add(3)
        self._binary_tree.add(2)
        self._binary_tree.add(1)
        assert(self._binary_tree.contains(1))
        assert(self._binary_tree.contains(2))
        assert(self._binary_tree.contains(3))
        assert(self._binary_tree.contains(4))
        assert(self._binary_tree.contains(5))
        assert(self._binary_tree.contains(6))
        assert(self._binary_tree.contains(7))
        self.assertFalse(self._binary_tree.contains(8))

    def test_contains_values_in_right_unbalanced_tree(self):
        self._binary_tree.add(1)
        self._binary_tree.add(2)
        self._binary_tree.add(3)
        self._binary_tree.add(4)
        self._binary_tree.add(5)
        self._binary_tree.add(6)
        self._binary_tree.add(7)
        assert(self._binary_tree.contains(1))
        assert(self._binary_tree.contains(2))
        assert(self._binary_tree.contains(3))
        assert(self._binary_tree.contains(4))
        assert(self._binary_tree.contains(5))
        assert(self._binary_tree.contains(6))
        assert(self._binary_tree.contains(7))
        self.assertFalse(self._binary_tree.contains(8))

    def test_remove_item_not_in_tree_throws_exception(self):
        self.assertRaises(Exception, self._binary_tree.remove, 1)

    def test_remove_root(self):
        self._binary_tree.add(1)
        assert(self._binary_tree._counter == 1)
        self._binary_tree.remove(1)
        assert(self._binary_tree._root == None)
        assert(self._binary_tree._counter == 0)

    def test_remove_node_with_no_right_child(self):
        self._binary_tree.add(2)
        self._binary_tree.add(1)
        assert(self._binary_tree._root.right == None)
        assert(self._binary_tree._counter == 2)
        self._binary_tree.remove(2)
        assert(self._binary_tree._counter == 1)
        assert(self._binary_tree._root.value == 1)
        self.assertFalse(self._binary_tree.contains(2))

    def test_remove_node_where_right_child_has_no_left_child(self):
        self._binary_tree.add(4)
        self._binary_tree.add(3)
        self._binary_tree.add(5)
        self._binary_tree.add(1)
        self._binary_tree.add(2)
        self._binary_tree.add(7)
        self._binary_tree.add(8)
        assert(self._binary_tree._root.value == 4)
        assert(self._binary_tree._root.right.right.value == 7)
        assert(self._binary_tree._root.right.right.right.value == 8)
        assert(self._binary_tree._counter == 7)
        assert(self._binary_tree._root.right.value == 5)
        self._binary_tree.remove(5)
        assert(self._binary_tree._root.right.value == 7)
        assert(self._binary_tree._root.right.right.value == 8)

    def test_remove_node_where_right_child_has_a_left_child(self):
        self._binary_tree.add(4)
        self._binary_tree.add(3)
        self._binary_tree.add(6)
        self._binary_tree.add(1)
        self._binary_tree.add(2)
        self._binary_tree.add(7)
        self._binary_tree.add(5)
        assert(self._binary_tree._counter == 7)
        assert(self._binary_tree._root.value == 4)
        assert(self._binary_tree._root.right.value == 6)
        assert(self._binary_tree._root.right.right.value == 7)
        self._binary_tree.remove(6)
        assert(self._binary_tree._counter == 6)
        assert(self._binary_tree._root.value == 4)
        assert(self._binary_tree._root.right.value == 7)
        assert(self._binary_tree._root.right.left.value == 5)

    def test_pre_order_traversal(self):
        self._binary_tree.add(4)
        self._binary_tree.add(2)
        self._binary_tree.add(6)
        self._binary_tree.add(1)
        self._binary_tree.add(3)
        self._binary_tree.add(5)
        self._binary_tree.add(7)
        pre_order = self._binary_tree.values_pre_order(self._binary_tree._root)
        post_order = self._binary_tree.values_post_order(self._binary_tree._root)
        in_order = self._binary_tree.values_in_order(self._binary_tree._root)
        parents_first = [4, 2, 1, 3, 6, 5, 7]
        children_first = [1, 3, 2, 5, 7, 6, 4]
        sort_order = [1, 2, 3, 4, 5, 6, 7]
        assert(pre_order == parents_first)
        assert(post_order == children_first)
        assert(in_order == sort_order)
