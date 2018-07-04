import unittest

from structures.set import Set

class TestSet(unittest.TestCase):
    def setUp(self):
        self._set = Set()

    def test_add_item_increases_count(self):
        assert(self._set.count() == 0)
        self._set.add(1)
        assert(self._set.count() == 1)

    def test_add_range(self):
        assert(self._set.count() == 0)
        self._set.add_range([1, 2, 3, 4, 5])
        assert(self._set.count() == 5)

    def test_add_range_with_duplicates(self):
        assert(self._set.count() == 0)
        self._set.add(1)
        self._set.add_range([1, 2, 2, 3])
        assert(self._set.count() == 3)

    def test_remove_resduces_count(self):
        assert(self._set.count() == 0)
        self._set.add(1)
        assert(self._set.count() == 1)
        self._set.remove(1)
        assert(self._set.count() == 0)

    def test_remove_item(self):
        self._set.add(1)
        assert(self._set.contains(1))
        self._set.remove(1)
        self.assertFalse(self._set.contains(1))

    def test_contains(self):
        self._set.add(1)
        assert(self._set.contains(1))
        self.assertFalse(self._set.contains(2))

    def test_enumerator(self):
        range = [1, 2, 3]
        self._set.add_range(range)
        for i, j in self._set.enumerator():
            assert(j == range[i])

    def test_union(self):
        set = Set()
        self._set.add_range([1, 2, 3])
        set.add_range([3, 4, 5])
        union_set = self._set.union(set)
        assert(union_set.count() == 5)
        assert(self._set.count() == 3)
        assert(set.count() == 3)

    def test_intersection(self):
        set = Set()
        self._set.add_range([1, 2, 3])
        set.add_range([3, 4, 5])
        intersection_set = self._set.intersection(set)
        assert(intersection_set.count() == 1)
        assert(intersection_set.contains(3))
        assert(self._set.count() == 3)
        assert(set.count() == 3)

    def test_difference(self):
        set = Set()
        self._set.add_range([1, 2, 3])
        set.add_range([3, 4, 5])
        difference_set = self._set.difference(set)
        assert(difference_set.count() == 2)
        assert(difference_set.contains(1))
        assert(difference_set.contains(2))
        assert(self._set.count() == 3)
        assert(set.count() == 3)

    def test_symmetric_difference(self):
        set = Set()
        self._set.add_range([1, 2, 3])
        set.add_range([3, 4, 5])
        symmetric_difference_set = self._set.symmetric_difference(set)
        assert(symmetric_difference_set.count() == 4)
        assert(symmetric_difference_set.contains(1))
        assert(symmetric_difference_set.contains(2))
        self.assertFalse(symmetric_difference_set.contains(3))
        assert(symmetric_difference_set.contains(4))
        assert(symmetric_difference_set.contains(5))
        assert(self._set.count() == 3)
        assert(set.count() == 3)
