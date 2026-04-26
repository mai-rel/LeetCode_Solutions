from collections import deque
from typing import List


def count_cells(grid, m, n, i, j):
    queue = deque([(i, j)])
    count = 1
    grid[i][j] = 0

    while queue:
        row, col = queue.popleft()

        for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            next_row = row + dr
            next_col = col + dc

            if not (0 <= next_row < m and 0 <= next_col < n):
                continue

            if grid[next_row][next_col] == 1:
                count += 1
                grid[next_row][next_col] = 0
                queue.append((next_row, next_col))

    return count


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    max_count = 0

    for i, row in enumerate(grid):
        for j, value in enumerate(row):

            if value == 0:
                continue

            count = count_cells(grid, m, n, i, j)
            max_count = max(max_count, count)

    return max_count