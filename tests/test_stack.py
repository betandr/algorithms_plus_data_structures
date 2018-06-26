import unittest

from structures.stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self):
        self._stack = Stack()

    def test_pop_from_empty_stack_raises_index_error(self):
        self.assertRaises(IndexError, self._stack.pop)

    def test_pop_from_empty_stack_which_had_items_raises_index_error(self):
        self._stack.push(1)
        self._stack.pop()
        self.assertRaises(IndexError, self._stack.pop)

    def test_pop_returns_items_in_order(self):
        self._stack.push(3)
        self._stack.push(2)
        self._stack.push(1)
        assert(self._stack.pop() == 1)
        assert(self._stack.pop() == 2)
        assert(self._stack.pop() == 3)

    def test_peek_returns_top_item(self):
        self._stack.push(2)
        self._stack.push(1)
        assert(self._stack.peek() == 1)

    def test_peek_leaves_item_on_stack(self):
        self._stack.push(1)
        assert(self._stack.peek() == 1)
        assert(self._stack.pop() == 1)
