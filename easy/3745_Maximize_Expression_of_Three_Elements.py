from typing import List


def maximizeExpressionOfThree(nums: List[int]) -> int:
    nums.sort()
    return nums[-2] + nums[-1] - nums[0]


