

class AVLTreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value

    def is_greater_than(self, node):
        if(self.value > node.value):
            return True
        else:
            return False

    def is_less_than(self, node):
        if(self.value < node.value):
            return True
        else:
            return False

    def left_height(self):
        return self._max_child_height(self.left)

    def right_height(self):
        return self._max_child_height(self.right)

    def _max_child_height(self, node):
        if node is not None:
            max_left = self._max_child_height(node.left)
            max_right = self._max_child_height(node.right)
            return 1 + max(max_left, max_right)
        else:
            return 0

    def balance_factor(self):
        return self.right_height() - self.left_height()

    def state(self):
        if self.balance_factor() > 1:
            return AVLTree.RIGHT_HEAVY
        elif self.balance_factor() < -1:
            return AVLTree.LEFT_HEAVY
        else:
            return AVLTree.BALANCED

class AVLTree:
    LEFT_HEAVY = 0
    RIGHT_HEAVY = 1
    BALANCED = 2
    def __init__(self):
        self._root = None
        self._counter = 0

    def _rotate_right(self, node):
        temp = self._root
        self._root = temp.left
        temp.left = self._root.right
        self._root.right = temp

    def _rotate_left(self, node):
        temp = self._root
        self._root = temp.right
        temp.right = self._root.left
        self._root.left = temp

    def _rotate_right_left(self, node):
        self._rotate_left(self._root.left)
        self._rotate_right(self._root)

    def _rotate_left_right(self, node):
        self._rotate_right(self._root.right)
        import pdb; pdb.set_trace()
        self._rotate_left(self._root)

    def balance(self, node):
        if node.state() == AVLTree.RIGHT_HEAVY:
            if node.right is not None and node.right.balance_factor() < 0:
                self._rotate_left_right(node)
            else:
                self._rotate_left(node)
        elif node.state() == AVLTree.LEFT_HEAVY:
            if node.left is not None and node.left.balance_factor() > 0:
                self._rotate_right_left(node)
            else:
                self._rotate_right(node)

    def _add_to(self, node, value):
        new_node = AVLTreeNode(value)
        if new_node.is_less_than(node):
            if node.left == None :
                node.left = new_node
                new_node.parent = node
            else:
                self._add_to(node.left, value)
        else:
            if node.right == None:
                node.right = new_node
                new_node.parent = node
            else:
                self._add_to(node.right, value)
        self.balance(new_node)

    def add(self, value):
        if (self._root == None):
            self._root = AVLTreeNode(value)
        else:
            self._add_to(self._root, value)

        self._counter += 1

    def _find_from_parent(self, node, value):
        current = self._root
        parent = None
        find_node = AVLTreeNode(value)

        while(current != None):
            if find_node.is_less_than(current):
                parent = current
                current = current.left
            elif find_node.is_greater_than(current):
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
            raise Exception("{} does not exist in tree.".format(value))

        # Case 1: AVLTreeNode has no right child, so node's left replaces node
        if (node.right == None):
            if (parent == None):
                self._root = node.left
            else:
                if parent.is_greater_than(node):
                    parent.left = node.left
                elif parent.is_less_than(node):
                    parent.right = node.left
        # Case 2: AVLTreeNode's right child has no left child, so node's right child replaces node
        elif (node.right.left == None):
            node.right.left = node.left
            if (parent == None):
                self._root = node.right
            else:
                if parent.is_greater_than(node):
                    parent.left = node.right
                elif parent.is_less_than(node):
                    parent.right = node.right
        # Case 3: AVLTreeNode's right child has a left child, so node's right child's left most child replaces node
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
                if parent.is_greater_than(node):
                    parent.left = leftmost
                elif parent.is_less_than(node):
                    parent.right = leftmost

        self.balance(parent)
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
