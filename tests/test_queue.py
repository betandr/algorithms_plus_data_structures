import unittest

from structures.queue import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self._queue = Queue()

    def test_enqueue_and_peek(self):
        self._queue.enqueue(1)
        assert (self._queue.peek() == 1)

    def test_enqueue_many_and_peek(self):
        self._queue.enqueue(1)
        self._queue.enqueue(2)
        self._queue.enqueue(3)
        assert (self._queue.peek() == 1)

    def test_dequeue_from_empty_queue(self):
        self.assertRaises(IndexError, self._queue.dequeue)

    def test_enqueue_and_dequeue_in_correct_order(self):
        self._queue.enqueue(1)
        self._queue.enqueue(2)
        self._queue.enqueue(3)
        assert(self._queue.dequeue() == 1)
        assert(self._queue.dequeue() == 2)
        assert(self._queue.dequeue() == 3)

    def test_peek_does_not_change_state(self):
        self._queue.enqueue(1)
        self._queue.enqueue(2)
        assert (self._queue.peek() == 1)
        assert (self._queue.peek() == 1)
        self._queue.dequeue()
        assert (self._queue.peek() == 2)
        assert (self._queue.peek() == 2)
