import unittest

from algorithms.binary_search import binary_search

class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        t = 8
        a = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

        i = binary_search(a, t)

        assert t == a[i]

    def test_not_found(self):
        t = 3
        a = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

        i = binary_search(a, t)

        assert None == i
