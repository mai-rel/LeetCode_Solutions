from typing import List
from math import inf


def minSubArrayLen(target: int, nums: List[int]) -> int:
    min_len = inf
    total = 0
    l = 0

    for r, num in enumerate(nums):
        total += num
        if total < target:
            continue

        while total >= target:
            min_len = min(min_len, r - l + 1)
            total -= nums[l]
            l += 1

    return 0 if min_len == inf else min_len