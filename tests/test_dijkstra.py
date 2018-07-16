import unittest
from decimal import Decimal

from algorithms.dijkstra import Graph, Node, Edge, dijkstra, min_dist, to_array

# result, distance = shortest_path(g, a)
# path = [node.label for node in result]
# route = " -> ".join(path)
# print("The ideal route is {} with distance of {}".format(route, distance))

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self._graph = Graph()
        self._node_a = Node("A")
        self._graph.add_node(self._node_a)
        self._node_b = Node("B")
        self._graph.add_node(self._node_b)
        self._node_c = Node("C")
        self._graph.add_node(self._node_c)
        self._node_d = Node("D")
        self._graph.add_node(self._node_d)
        self._node_e = Node("E")
        self._graph.add_node(self._node_e)
        self._node_f = Node("F")
        self._graph.add_node(self._node_f)
        self._node_g = Node("G")
        self._graph.add_node(self._node_g)

        self._graph.add_edge(self._node_a, self._node_b, 4)
        self._graph.add_edge(self._node_a, self._node_c, 3)
        self._graph.add_edge(self._node_a, self._node_e, 7)
        self._graph.add_edge(self._node_b, self._node_c, 6)
        self._graph.add_edge(self._node_b, self._node_d, 5)
        self._graph.add_edge(self._node_c, self._node_d, 11)
        self._graph.add_edge(self._node_c, self._node_e, 8)
        self._graph.add_edge(self._node_d, self._node_e, 2)
        self._graph.add_edge(self._node_d, self._node_f, 2)
        self._graph.add_edge(self._node_d, self._node_g, 10)
        self._graph.add_edge(self._node_e, self._node_g, 5)
        self._graph.add_edge(self._node_f, self._node_g, 3)

    def test_correct_number_nodes(self):
        assert 7 == len(self._graph.nodes)

    def test_correct_number_edges(self):
        assert 6 == len(self._graph.edges)
        assert 3 == len(self._graph.edges['A'])
        assert 2 == len(self._graph.edges['B'])
        assert 2 == len(self._graph.edges['C'])
        assert 3 == len(self._graph.edges['D'])
        assert 1 == len(self._graph.edges['E'])
        assert 1 == len(self._graph.edges['F'])

    def test_correct_edge_lengths(self):
        assert 4 == self._graph.edges['A']['B'].length
        assert 3 == self._graph.edges['A']['C'].length
        assert 7 == self._graph.edges['A']['E'].length
        assert 6 == self._graph.edges['B']['C'].length
        assert 5 == self._graph.edges['B']['D'].length
        assert 11 == self._graph.edges['C']['D'].length
        assert 8 == self._graph.edges['C']['E'].length
        assert 2 == self._graph.edges['D']['E'].length
        assert 2 == self._graph.edges['D']['F'].length
        assert 10 == self._graph.edges['D']['G'].length
        assert 5 == self._graph.edges['E']['G'].length
        assert 3 == self._graph.edges['F']['G'].length

    def test_min_dist_with_nones(self):
        INFINITY = Decimal('Infinity')
        q = set()
        dist = {}

        a = Node("A")
        q.add(a)
        dist[a] = 0

        b = Node("B")
        q.add(b)
        dist[b] = INFINITY

        c = Node("C")
        q.add(c)
        dist[c] = INFINITY

        node = min_dist(q, dist)
        assert "A" == node.label

    def test_min_dist_with_values(self):
        q = set()
        dist = {}

        a = Node("A")
        q.add(a)
        dist[a] = 0

        b = Node("B")
        q.add(b)
        dist[b] = 4

        c = Node("C")
        q.add(c)
        dist[c] = 6

        node = min_dist(q, dist)
        assert "A" == node.label

    def test_previous_nodes(self):
        dist, prev = dijkstra(self._graph, self._node_a)
        # prev: F -> D -> B -> A
        d = prev[self._node_f]
        assert "D" == d.label

        b = prev[d]
        assert "B" == b.label

        a = prev[b]
        assert "A" == a.label

    def test_dist_nodes(self):
        dist, prev = dijkstra(self._graph, self._node_a)
        # dist: A -4-> B -5-> D -2-> F == 11
        assert 11 == dist[self._node_f]

    def test_prev_to_route_array(self):
        dist, prev = dijkstra(self._graph, self._node_a)
        assert ["A", "B", "D", "F"] == to_array(prev, self._node_f)
