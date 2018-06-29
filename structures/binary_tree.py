

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def is_smaller_than(self, node):
        if(self.value < node.value):
            return True
        else:
            return False


class BinaryTree:
    def __init__(self):
        self._root = None
        self._counter = 0

    def _add_to(self, node, value):
        if(value < node.value):
            if(node.left == None):
                node.left = Node(value)
            else:
                self._add_to(node.left, value)
        else:
            if(node.right == None):
                node.right = Node(value)
            else:
                self._add_to(node.right, value)

    def add(self, value):
        if (self._root == None):
            self._root = Node(value)
        else:
            self._add_to(self._root, value)

        self._counter += 1

    def _find_from_parent(self, node, value):
        current = self._root
        parent = None

        while(current != None):
            if(value < current.value ):
                parent = current
                current = current.left
            elif(value > current.value):
                parent = current
                current = current.right
            else:
                break

        return current, parent

    def contains(self, value):
        return self._find_from_parent(self._root, value)[0] != None

    def remove(self, value):
        node, parent = self._find_from_parent(self._root, value)

        if (node == None):
            raise Exception("Value does not exist in tree.")

        # Case 1: Node has no right child, so node's left replaces node
        if (node.right == None):
            if (parent == None):
                self._root = node.left
            else:
                if(parent.value > node.value):
                    parent.left = node.left
                elif(parent.value > node.value):
                    parent.right = node.left
        # Case 2: Node's right child has no left child, so node's right child replaces node
        elif (node.right.left == None):
            node.right.left = node.left
            if (parent == None):
                self._root = node.right
            else:
                if(parent.value > node.value):
                    parent.left = node.right
                elif(parent.value < node.value):
                    parent.right = node.right
        # Case 3: Node's right child has a left child, so node's right child's left most child replaces node
        else:
            leftmost = node.right.left
            leftmost_parent = node.right

            while (leftmost.left != None):
                leftmost_parent = leftmost
                leftmost = leftmost.left

            leftmost_parent.left = leftmost.right

            leftmost.left = node.left
            leftmost.right = node.right

            if(parent == None):
                self._root = leftmost
            else:
                if(parent.value > node.value):
                    parent.left = leftmost
                elif(parent.value < node.value):
                    parent.right = leftmost

        self._counter -= 1
        return True

    def _pre_order_traversal(self, node, l):
        if(node != None):
            l.append(node.value)
            self._pre_order_traversal(node.left, l)
            self._pre_order_traversal(node.right, l)

    def values_pre_order(self, node):
        values = []
        self._pre_order_traversal(node, values)
        return values

    def _post_order_traversal(self, node, l):
        if(node != None):
            self._post_order_traversal(node.left, l)
            self._post_order_traversal(node.right, l)
            l.append(node.value)

    def values_post_order(self, node):
        values = []
        self._post_order_traversal(node, values)
        return values

    def _in_order_traversal(self, node, l):
        if(node != None):
            self._in_order_traversal(node.left, l)
            l.append(node.value)
            self._in_order_traversal(node.right, l)

    def values_in_order(self, node):
        values = []
        self._in_order_traversal(node, values)
        return values
