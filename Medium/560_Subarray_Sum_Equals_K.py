from typing import List
from collections import defaultdict


def subarraySum(nums: List[int], k: int) -> int:
    prefixSums = defaultdict(int)
    prefixSums[0] = 1

    total = 0
    count = 0

    for num in nums:
        total += num
        target = total - k
        count += prefixSums[target]
        prefixSums[total] += 1

    return count