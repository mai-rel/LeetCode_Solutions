from collections import deque
from typing import List


def get_size(field, m, n, start_row, start_col):
    frontier = deque([(start_row, start_col)])
    island_size = 1
    field[start_row][start_col] = 0

    while frontier:
        row, col = frontier.popleft()

        for delta_row, delta_col in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            neighbor_row = row + delta_row
            neighbor_col = col + delta_col

            if not (0 <= neighbor_row < m and 0 <= neighbor_col < n):
                continue

            if field[neighbor_row][neighbor_col] == 1:
                island_size += 1
                field[neighbor_row][neighbor_col] = 0
                frontier.append((neighbor_row, neighbor_col))

    return island_size


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    max_island_size = 0

    for i, row in enumerate(grid):
        for j, value in enumerate(row):

            if value == 0:
                continue

            island_size = get_size(grid, m, n, i, j)
            max_island_size = max(max_island_size, island_size)

    return max_island_size