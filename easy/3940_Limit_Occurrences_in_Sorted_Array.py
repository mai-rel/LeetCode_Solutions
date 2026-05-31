def limitOccurrences(nums: list[int], k: int) -> list[int]:
    result = []
    n = len(nums)

    i = 0
    j = 0

    while i < n:
        num = nums[i]
        while j < n and num == nums[j]:
            j += 1
        result.extend([num] * min(k, j - i))
        i = j

    return result