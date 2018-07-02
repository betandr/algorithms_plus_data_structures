import unittest

from algorithms.sorting import bubble_sort, insertion_sort, selection_sort, merge_sort, quicksort

class TestSorting(unittest.TestCase):
    def setUp(self):
        self._unsorted = [4, 7, 1, 9, 3, 8, 6, 5, 2]
        self._sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_bubble_sort(self):
        sorted = bubble_sort(self._unsorted)
        assert(sorted[0] == 1)
        assert(sorted[1] == 2)
        assert(sorted[2] == 3)
        assert(sorted[3] == 4)
        assert(sorted[4] == 5)
        assert(sorted[5] == 6)
        assert(sorted[6] == 7)
        assert(sorted[7] == 8)
        assert(sorted[8] == 9)

    def test_insertion_sort(self):
        sorted = insertion_sort(self._unsorted)
        assert(sorted[0] == 1)
        assert(sorted[1] == 2)
        assert(sorted[2] == 3)
        assert(sorted[3] == 4)
        assert(sorted[4] == 5)
        assert(sorted[5] == 6)
        assert(sorted[6] == 7)
        assert(sorted[7] == 8)
        assert(sorted[8] == 9)

    def test_selection_sort(self):
        sorted = selection_sort(self._unsorted)
        assert(sorted[0] == 1)
        assert(sorted[1] == 2)
        assert(sorted[2] == 3)
        assert(sorted[3] == 4)
        assert(sorted[4] == 5)
        assert(sorted[5] == 6)
        assert(sorted[6] == 7)
        assert(sorted[7] == 8)
        assert(sorted[8] == 9)

    def test_merge_sort(self):
        sorted = merge_sort(self._unsorted)
        assert(sorted[0] == 1)
        assert(sorted[1] == 2)
        assert(sorted[2] == 3)
        assert(sorted[3] == 4)
        assert(sorted[4] == 5)
        assert(sorted[5] == 6)
        assert(sorted[6] == 7)
        assert(sorted[7] == 8)
        assert(sorted[8] == 9)

    def test_quick_sort(self):
        sorted = quicksort(self._unsorted)
        assert(sorted[0] == 1)
        assert(sorted[1] == 2)
        assert(sorted[2] == 3)
        assert(sorted[3] == 4)
        assert(sorted[4] == 5)
        assert(sorted[5] == 6)
        assert(sorted[6] == 7)
        assert(sorted[7] == 8)
        assert(sorted[8] == 9)
