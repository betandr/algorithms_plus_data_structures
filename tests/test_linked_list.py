import unittest

from structures.linked_list import Node, LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self._linked_list = LinkedList()

    def test_is_empty(self):
        assert(self._linked_list.is_empty())
        self._linked_list.add_head(Node(1))
        self.assertFalse(self._linked_list.is_empty())

    def test_empty_linked_list(self):
        empty = self._linked_list.linked_list_as_string()
        assert(self._linked_list._counter == 0)
        assert(empty == "HEAD -> TAIL")

    def test_add_node_to_head(self):
        self._linked_list.add_head(Node(1))
        assert(self._linked_list._counter == 1)
        s = self._linked_list.linked_list_as_string()
        assert(s == "HEAD -> 1 -> TAIL")

    def test_add_two_nodes_to_head(self):
        self._linked_list.add_head(Node(1))
        self._linked_list.add_head(Node(2))
        assert(self._linked_list._counter == 2)
        s = self._linked_list.linked_list_as_string()
        assert(s == "HEAD -> 2 -> 1 -> TAIL")

    def test_add_node_to_tail_of_empty_list(self):
        self._linked_list.add_head(Node(1))
        assert(self._linked_list._counter == 1)
        s = self._linked_list.linked_list_as_string()
        assert(s == "HEAD -> 1 -> TAIL")

    def test_add_node_to_tail_of_list_with_items(self):
        self._linked_list.add_head(Node(1))
        self._linked_list.add_head(Node(2))
        assert(self._linked_list._counter == 2)
        s = self._linked_list.linked_list_as_string()
        assert(s == "HEAD -> 2 -> 1 -> TAIL")
        self._linked_list.add_tail(Node(0))
        s = self._linked_list.linked_list_as_string()
        assert(s == "HEAD -> 2 -> 1 -> 0 -> TAIL")

    def test_add_multiple_tails(self):
        self._linked_list.add_tail(Node(1))
        self._linked_list.add_tail(Node(2))
        self._linked_list.add_tail(Node(3))
        self._linked_list.add_tail(Node(4))
        assert(self._linked_list._counter == 4)
        s = self._linked_list.linked_list_as_string()
        assert(s == "HEAD -> 1 -> 2 -> 3 -> 4 -> TAIL")

    def test_remove_tail_from_linked_list_with_one_item(self):
        self._linked_list.add_head(Node(1))
        assert(self._linked_list._counter == 1)
        s = self._linked_list.linked_list_as_string()
        assert(s == "HEAD -> 1 -> TAIL")
        self._linked_list.remove_tail()
        assert(self._linked_list._counter == 0)
        s = self._linked_list.linked_list_as_string()
        assert(s == "HEAD -> TAIL")

    def test_remove_tail_from_linked_list_with_two_items(self):
        self._linked_list.add_head(Node(1))
        self._linked_list.add_head(Node(2))
        assert(self._linked_list._counter == 2)
        s = self._linked_list.linked_list_as_string()
        assert(s == "HEAD -> 2 -> 1 -> TAIL")
        self._linked_list.remove_tail()
        assert(self._linked_list._counter == 1)
        s = self._linked_list.linked_list_as_string()
        assert(s == "HEAD -> 2 -> TAIL")

    def test_remove_tail_from_linked_list_with_three_items(self):
        self._linked_list.add_head(Node(1))
        self._linked_list.add_head(Node(2))
        self._linked_list.add_head(Node(3))
        assert(self._linked_list._counter == 3)
        s = self._linked_list.linked_list_as_string()
        assert(s == "HEAD -> 3 -> 2 -> 1 -> TAIL")
        self._linked_list.remove_tail()
        assert(self._linked_list._counter == 2)
        s = self._linked_list.linked_list_as_string()
        assert(s == "HEAD -> 3 -> 2 -> TAIL")

    def test_remove_head_from_linked_list_with_one_item(self):
        self._linked_list.add_head(Node(1))
        assert(self._linked_list._counter == 1)
        s = self._linked_list.linked_list_as_string()
        assert(s == "HEAD -> 1 -> TAIL")
        self._linked_list.remove_head()
        assert(self._linked_list._counter == 0)
        s = self._linked_list.linked_list_as_string()
        assert(s == "HEAD -> TAIL")

    def test_remove_head_from_linked_list_with_two_items(self):
        self._linked_list.add_head(Node(1))
        self._linked_list.add_head(Node(2))
        assert(self._linked_list._counter == 2)
        s = self._linked_list.linked_list_as_string()
        assert(s == "HEAD -> 2 -> 1 -> TAIL")
        self._linked_list.remove_head()
        assert(self._linked_list._counter == 1)
        s = self._linked_list.linked_list_as_string()
        assert(s == "HEAD -> 1 -> TAIL")

    def test_remove_head_from_linked_list_with_three_items(self):
        self._linked_list.add_head(Node(1))
        self._linked_list.add_head(Node(2))
        self._linked_list.add_head(Node(3))
        assert(self._linked_list._counter == 3)
        s = self._linked_list.linked_list_as_string()
        assert(s == "HEAD -> 3 -> 2 -> 1 -> TAIL")
        self._linked_list.remove_head()
        assert(self._linked_list._counter == 2)
        s = self._linked_list.linked_list_as_string()
        assert(s == "HEAD -> 2 -> 1 -> TAIL")

    def test_get_enumerator(self):
        self._linked_list.add_head(Node(1))
        self._linked_list.add_head(Node(2))
        self._linked_list.add_head(Node(3))
        assert(self._linked_list._counter == 3)
        enumerator = self._linked_list.enumerator()
        next = enumerator.get_next()
        assert(next.value == 3)
        next = enumerator.get_next()
        assert(next.value == 2)
        next = enumerator.get_next()
        assert(next.value == 1)
