class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Enumerator:
    def __init__(self, linked_list):
        self._current = None
        self._list = linked_list

    def get_next(self):
        if (self._current == None):
            self._current = self._list._head
        else:
            temp = self._current
            self._current = temp.next

        return self._current


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._counter = 0

    def enumerator(self):
        return Enumerator(self)

    def is_empty(self):
        if (self._counter < 1):
            return True
        else:
            return False

    def linked_list_as_string(self):
        """
        Renders a linked list as a string.
        """
        s = "HEAD"
        node = self._head
        while (node != None):
            s = "{} -> {}".format(s, node.value)
            node = node.next

        return "{} -> TAIL".format(s)

    def add_head(self, node):
        """
        Add a node to the head of the list.
        """
        temp = self._head
        self._head = node
        self._head.next = temp
        self._counter += 1
        if (self._counter == 1):
            self._tail = self._head

    def add_tail(self, node):
        """
        Add a node to the tail of the list.
        """
        if (self._counter == 0):
            self._head = node
            self._tail = node
        else:
            self._tail.next = node

        self._tail = node

        self._counter += 1

    def remove_tail(self):
        """
        Remove the node at the tail of the list. Requires looping through entire
        list so decreases in performance by O(n)
        """
        if (self._counter != 0):
            if (self._counter == 1):
                self._head = None
                self._tail = None
            else:
                current = self._head
                while(current.next != self._tail):
                    current = current.next
                current.next = None
                self._tail = current
            self._counter -= 1

    def remove_head(self):
        """
        Remove the node at the tail of the head.
        """
        if (self._counter != 0):
            self._head = self._head.next
            self._counter -= 1
            if(self._counter == 0):
                self._tail = None
