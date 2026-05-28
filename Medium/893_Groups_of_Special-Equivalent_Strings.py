from typing import List


def numSpecialEquivGroups(words: List[str]) -> int:
    groups = set()
    n = len(words[0])

    for word in words:
        odd_pos_chars = [word[i] for i in range(1, n, 2)]
        even_pos_chars = [word[i] for i in range(0, n, 2)]
        odd_pos_chars.sort()
        even_pos_chars.sort()

        key = tuple([''.join(even_pos_chars), ''.join(odd_pos_chars)])
        groups.add(key)

    return len(groups)