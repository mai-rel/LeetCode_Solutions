from math import inf


def shortestBeautifulSubstring(s: str, k: int) -> str:
    n = len(s)
    ones = [i for i in range(n) if s[i] == '1']
    m = len(ones)

    if m < k:
        return ''

    min_len = inf
    result = ''

    for i in range(k - 1, m):
        right = ones[i]
        left = ones[i - k + 1]

        length = right - left + 1

        if length < min_len:
            min_len = length
            result = s[left:right + 1]
        elif length == min_len:
            result = min(result, s[left:right + 1])

    return result