from decimal import Decimal

class Node:
    def __init__(self, label):
        self.label = label

class Edge:
    def __init__(self, to_node, length):
        self.to_node = to_node
        self.length = length


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = dict()

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, from_node, to_node, length):
        edge = Edge(to_node, length)
        if from_node.label in self.edges:
            from_node_edges = self.edges[from_node.label]
        else:
            self.edges[from_node.label] = dict()
            from_node_edges = self.edges[from_node.label]
        from_node_edges[to_node.label] = edge


def min_dist(q, dist):
    """
    Returns the node with the smallest distance in q.
    Implemented to keep the main algorithm clean.
    """
    min_node = None
    for node in q:
        if min_node == None:
            min_node = node
        elif dist[node] < dist[min_node]:
            min_node = node

    return min_node

INFINITY = Decimal('Infinity')

def dijkstra(graph, source):
    q = set()
    dist = {}
    prev = {}

    for v in graph.nodes:       # initialization
        dist[v] = INFINITY      # unknown distance from source to v
        prev[v] = INFINITY      # previous node in optimal path from source
        q.add(v)                # all nodes initially in q (unvisited nodes)

    # distance from source to source
    dist[source] = 0

    while q:
        # node with the least distance selected first
        u = min_dist(q, dist)

        q.remove(u)

        if u.label in graph.edges:
            for _, v in graph.edges[u.label].items():
                alt = dist[u] + v.length
                if alt < dist[v.to_node]:
                    # a shorter path to v has been found
                    dist[v.to_node] = alt
                    prev[v.to_node] = u

    return dist, prev


def to_array(prev, from_node):
    """Creates an ordered list of labels as a route."""
    previous_node = prev[from_node]
    route = [from_node.label]
    while previous_node != INFINITY:
        route.append(previous_node.label)
        temp = previous_node
        previous_node = prev[temp]

    route.reverse()
    return route


graph = Graph()
node_a = Node("A")
graph.add_node(node_a)
node_b = Node("B")
graph.add_node(node_b)
node_c = Node("C")
graph.add_node(node_c)
node_d = Node("D")
graph.add_node(node_d)
node_e = Node("E")
graph.add_node(node_e)
node_f = Node("F")
graph.add_node(node_f)
node_g = Node("G")
graph.add_node(node_g)

graph.add_edge(node_a, node_b, 4)
graph.add_edge(node_a, node_c, 3)
graph.add_edge(node_a, node_e, 7)
graph.add_edge(node_b, node_c, 6)
graph.add_edge(node_b, node_d, 5)
graph.add_edge(node_c, node_d, 11)
graph.add_edge(node_c, node_e, 8)
graph.add_edge(node_d, node_e, 2)
graph.add_edge(node_d, node_f, 2)
graph.add_edge(node_d, node_g, 10)
graph.add_edge(node_e, node_g, 5)
graph.add_edge(node_f, node_g, 3)

dist, prev = dijkstra(graph, node_a)

print("The quickest path from {} to {} is [{}] with a distance of {}".format(
    node_a.label,
    node_f.label,
    " -> ".join(to_array(prev, node_f)),
    str(dist[node_f])
    )
)
