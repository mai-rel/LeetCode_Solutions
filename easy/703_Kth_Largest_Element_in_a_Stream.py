from  typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.size = k
        self.stream = nums
        heapq.heapify(self.stream)

        while len(self.stream) > k:
            heapq.heappop(self.stream)

    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val)
        if len(self.stream) > self.size:
            heapq.heappop(self.stream)

        return self.stream[0]

