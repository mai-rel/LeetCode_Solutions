from typing import List


def count_stores(items, max_products):
    stores = 0

    for i, count in enumerate(items):
        if count <= max_products:
            stores += 1
        else:
            stores += count // max_products
            if count % max_products:
                stores += 1

    return stores


def minimizedMaximum(n: int, quantities: List[int]) -> int:
    l = 1
    r = max(quantities)

    while l < r:
        m = (l + r) // 2
        if count_stores(quantities, m) > n:
            l = m + 1
        else:
            r = m

    return l