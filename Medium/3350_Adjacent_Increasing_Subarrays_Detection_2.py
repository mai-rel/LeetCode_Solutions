from  typing import List


def maxIncreasingSubarrays(nums: List[int]) -> int:
    n = len(nums)
    left_sizes = [1] * n

    for i in range(1, n):
        if nums[i - 1] < nums[i]:
            left_sizes[i] = left_sizes[i - 1] + 1

    right_size = 1
    max_k = 1

    for j in range(n - 2, -1, -1):
        max_size = min(right_size, left_sizes[j])
        max_k = max(max_k, max_size)
        if nums[j] < nums[j + 1]:
            right_size += 1
        else:
            right_size = 1

    return max_k