import unittest

from structures.hash_table import AdditiveHash, FoldingHash, AdditiveHashTable

class TestHashing(unittest.TestCase):

    def test_additive_hash(self):
        hash = AdditiveHash("foo")
        assert(hash.key == 324)

    def test_additive_hash_is_not_invariant(self):
        hash_foo = AdditiveHash("foo")
        hash_oof = AdditiveHash("oof")
        assert(hash_foo.key == hash_oof.key)

    def test_folding_hash(self):
        hash_one = FoldingHash("foobarbazqux")
        assert(hash_one.key == 36035133936893943449394333333306L)
        hash_two = FoldingHash("foobarbazqux")
        assert(hash_two.key == 36035133936893943449394333333306L)

    def test_folding_hash_is_invariant(self):
        forward_hash = FoldingHash("foobarbazqux")
        backward_hash = FoldingHash("xuqzabraboof")
        assert(forward_hash != backward_hash)

    def test_additive_hash_table_returns_value(self):
        hash_table = AdditiveHashTable()
        value = "foobarbazqux"
        hash_table.add(value)
        item = hash_table.get(value)
        assert(item == value)

    def test_additive_hash_table_returns_two_value(self):
        hash_table = AdditiveHashTable()
        value_one = "foo"
        value_two = "bar"
        hash_table.add(value_one)
        hash_table.add(value_two)
        item_one = hash_table.get(value_one)
        item_two = hash_table.get(value_two)
        assert(item_one == value_one)
        assert(item_two == value_two)
