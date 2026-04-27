from typing import List


def maxChunksToSorted(arr: List[int]) -> int:
    min_value = 0
    max_value = 0

    count = 0
    seen = set()

    for value in arr:
        seen.add(value)
        max_value = max(max_value, value)

        if min_value in seen and max_value in seen and len(seen) == max_value - min_value + 1:
            count += 1
            min_value = max_value + 1
            max_value = max_value + 1
            seen.clear()

    return count