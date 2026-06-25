from typing import List
import heapq


def smallestTrimmedNumbers(nums: List[str], queries: List[List[int]]) -> List[int]:
    heap = [(-trim, k, i) for i, (k, trim) in enumerate(queries)]
    heapq.heapify(heap)

    size = len(nums[0])
    nums = [[num, i] for i, num in enumerate(nums)]
    nums.sort()
    answer = [0] * len(queries)

    while heap:
        trim, k, index = heapq.heappop(heap)
        trim = -trim

        if trim < size:
            nums.sort(key=lambda x: (x[0][-trim:], x[1]))
            size = trim

        answer[index] = nums[k - 1][1]

    return answer