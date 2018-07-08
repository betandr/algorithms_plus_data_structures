import unittest

from algorithms.string_search import SearchMatch, NaiveSearch, BoyerMooreHorspoolSearch

class TestStringSearch(unittest.TestCase):
    def setUp(self):
        self._sentence = "Phasellus eget eros auctor, lobortis ligula eget, feugiat enim."
        self._contains_word = "ligula"
        self._does_not_contain_word = "foobarbaz"

    def test_naive_search(self):
        naive = NaiveSearch()
        match = naive.search(self._contains_word, self._sentence)
        assert match.start == 37
        assert match.length == len(self._contains_word)
        match = naive.search(self._does_not_contain_word, self._sentence)
        assert match is None

    def test_boyer_moor_horspool_bad_match_table(self):
        bmh = BoyerMooreHorspoolSearch()
        default_value, bad_match_table = bmh._build_bad_match_table(self._contains_word)
        assert bad_match_table['l'] == 1
        assert bad_match_table['i'] == 4
        assert bad_match_table['g'] == 3
        assert bad_match_table['u'] == 2
        assert bad_match_table['l'] == 1
        assert default_value == 6

    def test_boyer_moor_horspool_search(self):
        bmh = BoyerMooreHorspoolSearch()
        matches = bmh.search(self._contains_word, self._sentence)
        assert len(matches) == 1
        assert matches[0].start == 37
        assert matches[0].length == len(self._contains_word)
        matches = bmh.search(self._does_not_contain_word, self._sentence)
        assert len(matches) == 0

    def test_multi_result_boyer_moor_horspool_search(self):
        bmh = BoyerMooreHorspoolSearch()
        matches = bmh.search("eget", self._sentence)
        assert len(matches) == 2
        assert matches[0].start == 10
        assert matches[1].start == 44
