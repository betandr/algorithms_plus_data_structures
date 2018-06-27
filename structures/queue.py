from structures.linked_list import Node, LinkedList


class Queue:
    def __init__(self):
        self._linked_list = LinkedList()

    def enqueue(self, item):
        self._linked_list.add_tail(Node(item))

    def dequeue(self):
        if (self._linked_list.is_empty()):
            raise IndexError("Dequeue from empty queue")
        else:
            value = self._linked_list._head.value
            self._linked_list.remove_head()
            return value

    def peek(self):
        if (self._linked_list.is_empty()):
            raise IndexError("Peek from empty queue")
        else:
            return self._linked_list._head.value
