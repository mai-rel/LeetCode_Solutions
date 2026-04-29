from typing import List
from collections import Counter

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.counter1 = Counter(nums1)
        self.counter2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_value = self.nums2[index]
        self.counter2[old_value] -= 1
        self.nums2[index] += val
        self.counter2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        pairs = 0
        for num in self.counter1:
            need_num = tot - num
            if need_num in self.counter2:
                pairs += self.counter1[num] * self.counter2[need_num]

        return pairs