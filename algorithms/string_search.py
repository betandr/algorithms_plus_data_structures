
class SearchMatch:
    def __init__(self, start, length):
        self.start = start
        self.length = length


class NaiveSearch:
    def search(self, pattern, s):
        for i, c in enumerate(s):
            count = 0
            while s[i + count] == pattern[count]:
                count += 1
                if len(pattern) == count:
                    return SearchMatch(i, count)


class BoyerMooreHorspoolSearch:
    def _build_bad_match_table(self, pattern):
        default_value = len(pattern)
        distances = {}

        for i in range(0, len(pattern) - 1):
            distances[pattern[i]] = len(pattern) - i - 1
        return default_value, distances

    def search(self, pattern, to_search):
        matches = []
        default_value, bad_match_table = self._build_bad_match_table(pattern)
        current_start_index = 0
        while current_start_index <= len(to_search) - len(pattern):
            characters_to_match = len(pattern) - 1
            while characters_to_match >= 0 and pattern[characters_to_match] == to_search[current_start_index + characters_to_match]:
                characters_to_match -= 1
            if characters_to_match < 0:
                matches.append(SearchMatch(current_start_index, len(pattern)))
                current_start_index += len(pattern)
            else:
                current_start_index += bad_match_table.get(to_search[current_start_index + len(pattern) - 1], default_value)
        return matches
