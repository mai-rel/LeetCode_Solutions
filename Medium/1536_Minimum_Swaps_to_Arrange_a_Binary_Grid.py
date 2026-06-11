from typing import List


def swap_rows(zeros, i, j):
    for row in range(j, i, -1):
        zeros[row], zeros[row - 1] = zeros[row - 1], zeros[row]


def minSwaps(grid: List[List[int]]) -> int:
    n = len(grid)

    last_zeros = [0] * n

    for i in range(n):
        j = n - 1
        while j >= 0 and grid[i][j] == 0:
            j -= 1
        last_zeros[i] = n - j - 1

    swaps = 0
    target_zeros = n

    for i in range(n - 1):
        target_zeros -= 1
        if last_zeros[i] >= target_zeros:
            continue

        is_found = False

        for j in range(i + 1, n):
            if last_zeros[j] >= target_zeros:
                swaps += j - i
                swap_rows(last_zeros, i, j)
                is_found = True
                break

        if not is_found:
            return -1

    return swaps