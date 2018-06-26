from structures.linked_list import Node, LinkedList

class Stack:
    """
    Stack implemented with a linked list. This means no size limit or initial
    allocation as in an array, although memory is allocated on every push so
    could be less performant than an array-backed stack.

    An array-backed stack would need re-allocation of arrays to contain the
    stack items but this would be done every n pushes to the stack, where n is
    the frequency that the array should be re-allocated rather than on every push.
    """
    def __init__(self):
        self._linked_list = LinkedList()

    def push(self, item):
        self._linked_list.add_head(Node(item))

    def pop(self):
        if (self._linked_list.is_empty()):
            raise IndexError("Pop from empty stack")
        else:
            value = self.peek()
            self._linked_list.remove_head()
            return value

    def peek(self):
        if (self._linked_list.is_empty()):
            raise IndexError("Peek from empty stack")
        else:
            return self._linked_list._head.value
