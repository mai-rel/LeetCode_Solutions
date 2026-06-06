from typing import List


def leftRightDifference(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0] * n

    leftSum = 0

    for i, num in enumerate(nums):
        result[i] = leftSum
        leftSum += num

    rightSum = 0

    for i in range(n - 1, -1, -1):
        result[i] = abs(result[i] - rightSum)
        rightSum += nums[i]

    return result