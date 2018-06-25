import unittest

from structures.node_chain import Node
from structures.node_chain import nodes_to_string

class TestNodeChain(unittest.TestCase):

    def test_add_single_node(self):
        first = Node(1)
        assert nodes_to_string(first) == "1"

    def test_add_two_nodes(self):
        first = Node(1)
        middle = Node(2)
        first.next = middle
        assert nodes_to_string(first) == "1 -> 2"

    def test_add_three_nodes(self):
        first = Node(1)
        middle = Node(2)
        last = Node(3)
        first.next = middle
        middle.next = last
        assert(nodes_to_string(first) == "1 -> 2 -> 3")

if __name__ == "__main__":
    unittest.main()
