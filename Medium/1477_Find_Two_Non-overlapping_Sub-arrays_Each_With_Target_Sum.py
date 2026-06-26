from typing import List
from math import inf


def minSumOfLengths(arr: List[int], target: int) -> int:
    prefixLens = [0]
    n = len(arr)

    prefixSums = {0: -1}
    total = 0

    for i, num in enumerate(arr):
        total += num
        need_sum = total - target

        min_len = prefixLens[-1]

        if need_sum in prefixSums:
            cur_len = i - prefixSums[need_sum]
            if not min_len or min_len > cur_len:
                min_len = cur_len

        prefixLens.append(min_len)
        prefixSums[total] = i

    result = inf
    prefixSums = {0: n}
    total = 0
    best_start_len = 0

    for i in range(n - 1, -1, -1):
        total += arr[i]
        need_sum = total - target
        if need_sum in prefixSums:
            cur_len = prefixSums[need_sum] - i
            if not best_start_len or best_start_len > cur_len:
                best_start_len = cur_len

        best_end_len = prefixLens[i]

        if best_end_len and best_start_len:
            result = min(result, best_start_len + best_end_len)

        prefixSums[total] = i

    return -1 if result == inf else result