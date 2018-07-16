

def binary_search(a, t):
    l = 0
    r = len(a)
    while l <= r:
        m = (l + r) // 2
        if a[m] < t:
            l = m + 1
        elif a[m] > t:
            r = m - 1
        else:
            return m
