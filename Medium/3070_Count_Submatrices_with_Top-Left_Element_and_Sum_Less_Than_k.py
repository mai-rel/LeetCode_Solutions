from typing import List


def countSubmatrices(grid: List[List[int]], k: int) -> int:
    m = len(grid)
    n = len(grid[0])

    cols_sum = [0] * n
    valid_submatrices = 0

    for i, row in enumerate(grid):
        total = 0

        for j, value in enumerate(row):
            cols_sum[j] += value
            total += cols_sum[j]
            if total <= k:
                valid_submatrices += 1

    return valid_submatrices