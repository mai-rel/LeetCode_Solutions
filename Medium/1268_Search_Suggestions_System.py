from typing import List


def get_first(words, prefix, l, r):
    while l < r:
        m = (l + r) // 2
        if words[m] >= prefix:
            r = m
        else:
            l = m + 1
    return l


def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
    products.sort()
    l = 0
    n = len(products)
    r = n - 1

    result = [[] for _ in range(len(searchWord))]

    prefix = ''
    for j, char in enumerate(searchWord):

        prefix += char
        pos = get_first(products, prefix, l, r)

        for i in range(pos, min(pos + 3, n)):
            word = products[i]
            if word.startswith(prefix):
                result[j].append(word)
            else:
                break

        if not result[j]:
            break

        l = pos

    return result