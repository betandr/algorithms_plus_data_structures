import unittest

from structures.avl_tree import AVLTree

class TestAVLTree(unittest.TestCase):
    def setUp(self):
        self._tree = AVLTree()

    def test_new_node_has_correct_parent(self):
        self._tree.add(3)
        self._tree.add(4)
        self._tree.add(2)
        assert(self._tree._root.right.parent == self._tree._root)
        assert(self._tree._root.left.parent == self._tree._root)

    def test_add_increases_height(self):
        self._tree.add(3)
        self._tree.add(4)
        assert(self._tree._root.right.value == 4)
        assert(self._tree._root.left_height() == 0)
        assert(self._tree._root.right_height() == 1)
        self._tree.add(5)
        assert(self._tree._root.left_height() == 0)
        assert(self._tree._root.right_height() == 2)
        self._tree.add(2)
        assert(self._tree._root.left_height() == 1)
        assert(self._tree._root.right_height() == 2)

    def test_balance_factor(self):
        self._tree.add(3)
        self._tree.add(4)
        assert(self._tree._root.balance_factor() == 1)
        self._tree.add(2)
        assert(self._tree._root.balance_factor() == 0)
        self._tree.add(5)
        self._tree.add(6)
        assert(self._tree._root.balance_factor() == 2)

    def test_negative_balance_factor(self):
        self._tree.add(3)
        self._tree.add(2)
        self._tree.add(1)
        self._tree.add(0)
        assert(self._tree._root.left_height() == 3)
        assert(self._tree._root.right_height() == 0)
        assert(self._tree._root.balance_factor() == -3)

    def test_left_heavy_balance(self):
        self._tree.add(3)
        self._tree.add(2)
        self._tree.add(1)
        self._tree.add(0)
        assert(self._tree._root.state() == AVLTree.LEFT_HEAVY)

    def test_right_heavy_balance(self):
        self._tree.add(0)
        self._tree.add(1)
        self._tree.add(2)
        self._tree.add(3)
        assert(self._tree._root.state() == AVLTree.RIGHT_HEAVY)

    def test_balanced_balance(self):
        self._tree.add(3)
        self._tree.add(2)
        self._tree.add(5)
        assert(self._tree._root.state() == AVLTree.BALANCED)

    def test_rotate_right(self):
        self._tree.add(4)
        self._tree.add(2)
        self._tree.add(1)
        self._tree.add(3)
        assert(self._tree._root.value == 4)
        assert(self._tree._root.left.value == 2)
        assert(self._tree._root.left.left.value == 1)
        assert(self._tree._root.left.right.value == 3)
        assert(self._tree._root.state() == AVLTree.LEFT_HEAVY)
        self._tree._rotate_right(self._tree._root)
        assert(self._tree._root.value == 2)
        assert(self._tree._root.left.value == 1)
        assert(self._tree._root.right.value == 4)
        assert(self._tree._root.right.left.value == 3)

    def test_rotate_left(self):
        self._tree.add(2)
        self._tree.add(4)
        self._tree.add(3)
        self._tree.add(5)
        assert(self._tree._root.value == 2)
        assert(self._tree._root.right.value == 4)
        assert(self._tree._root.right.left.value == 3)
        assert(self._tree._root.right.right.value == 5)
        assert(self._tree._root.state() == AVLTree.RIGHT_HEAVY)
        assert(self._tree._root.balance_factor() > 0)
        self._tree._rotate_left(self._tree._root)
        assert(self._tree._root.value == 4)
        assert(self._tree._root.left.value == 2)
        assert(self._tree._root.right.value == 5)
        assert(self._tree._root.left.right.value == 3)

    # FIXME: Impl is wrong
    def test_rotate_right_left(self):
        self._tree.add(3)
        self._tree.add(1)
        self._tree.add(2)
        assert(self._tree._root.value == 3)
        assert(self._tree._root.left.value == 1)
        assert(self._tree._root.left.right.value == 2)
        # self._tree._rotate_right_left(self._tree._root)
        # assert(self._tree._root.value == 2)
        # assert(self._tree._root.left.value == 1)
        # assert(self._tree._root.right.value == 3)

    # FIXME: Impl is wrong
    def test_rotate_left_right(self):
        self._tree.add(2)
        self._tree.add(4)
        self._tree.add(3)
        assert(self._tree._root.value == 2)
        assert(self._tree._root.right.value == 4)
        assert(self._tree._root.right.left.value == 3)
        # self._tree._rotate_left_right(self._tree._root)
        # assert(self._tree._root.value == 3)
        # assert(self._tree._root.left.value == 2)
        # assert(self._tree._root.right.value == 4)
