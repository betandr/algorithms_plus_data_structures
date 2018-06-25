class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def print_nodes(node):
    """Prints the value of the current node and all further nodes"""
    while(node != None):
        print(node.value)
        if (node.next):
            print("|")
        node = node.next

first = Node(1)

middle = Node(2)
first.next = middle

last = Node(3)
middle.next = last

print_nodes(first)
