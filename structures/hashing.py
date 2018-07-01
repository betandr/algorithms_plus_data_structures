# Don't do this yourself, kids. Much smarter people have built hashing
# algorithms so just use those! ;)

class AdditiveHash:
    """
    Generate a hash using a very naive algorithm that adds the Unicode values of
    each character.
    Pro:
    - Stable
    - Efficient
    Cons:
    - Not Uniform: AdditiveHash("foo") == AdditiveHash("oof")
    - Not Secure
    """
    def __init__(self, s):
        """
        Generate a Hash object from a string, s
        """
        self.key = self._compute_hash(s)

    def _compute_hash(self, s):
        val = 0
        for c in s:
            val += ord(c)
        return val

class FoldingHash:
    """
    Generate a hash by folding a moving window of 4 characters together and then
    add to a rolling value.
    Pro:
    - Stable
    - Efficient
    - Uniform: AdditiveHash("foo") == AdditiveHash("oof")
    Cons:
    - Not Secure
    """
    def __init__(self, s):
        self.key = self._compute_hash(s)

    def _compute_hash(self, s):
        i = 0
        val = 0
        window = s[i:i+4]
        while(window > ''):
            temp = ''
            for c in s:
                temp = str(ord(c)) + temp
            val += int(temp)
            i += 4
            window = s[i:i+4]

        return val

class AdditiveHashTable:
    def __init__(self):
        self._table = [0, 0, 0, 0, 0, 0, 0, 0]

    def add(self, item):
        hash = AdditiveHash(item)
        index = hash.key % 8
        self._table[index] = item

    def get(self, item):
        hash = AdditiveHash(item)
        index = hash.key % 8
        return self._table[index]
