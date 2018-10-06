class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def nodes_to_string(node):
    """
    Renders nodes as a string, uses array N size number of nodes
    """
    nodes = []
    while(node != None):
        nodes.append(str(node.value))
        node = node.next
    return " -> ".join(nodes)
