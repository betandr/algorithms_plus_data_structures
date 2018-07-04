class Set:
    def __init__(self):
        self._list = []

    def add(self, item):
        if item not in self._list:
            self._list.append(item)

    def add_range(self, items):
        for item in items:
            self.add(item)

    def count(self):
        return len(self._list)

    def contains(self, item):
        return item in self._list

    def remove(self, item):
        if item in self._list:
            self._list.remove(item)

    def union(self, set):
        """
        Returns a set that contains all of the unique items in two other sets.
        {1, 2, 3} u {3, 4, 5} = {1, 2, 3, 4, 5}
        """
        s = Set()
        s.add_range(self._list)
        s.add_range(set._list)
        return s

    def intersection(self, set):
        """
        Returns a set that contains all of the intersecting members of two other sets.
        {1, 2, 3} n {3, 4, 5} = {3}
        """
        s = Set()
        for i, j in enumerate(set._list):
            if self.contains(j):
                s.add(j)
        return s

    def difference(self, set):
        """
        Returns a set that contains members of one set that are not members of a second set.
        {1, 2, 3} \ {3, 4, 5} = {1, 2}
        """
        sd = Set()
        sd.add_range(self._list)
        for i, j in enumerate(set._list):
            if set.contains(j):
                sd.remove(j)
        return sd

    def symmetric_difference(self, set):
        """
        Returns a set that contains members of two sets that are not in the other set.
        {1, 2, 3} /\ {3, 4, 5} = {1, 2, 4, 5}
        """
        d1 = self.difference(set)
        d2 = set.difference(self)
        return d1.union(d2)

    def enumerator(self):
        return enumerate(self._list)
