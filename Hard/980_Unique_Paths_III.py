from typing import List


def uniquePathsIII(grid: List[List[int]]) -> int:
    start = None
    end = None
    obstacles = set()
    m = len(grid)
    n = len(grid[0])

    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == -1:
                obstacles.add((i, j))
            elif not start and value == 1:
                start = (i, j)
            elif not end and value == 2:
                end = (i, j)

    count = 0
    walked = set()
    walked.add(start)
    distance = m * n - len(obstacles)

    def backtrack(m, n, i, j):
        nonlocal count
        if (i, j) == end:
            if len(walked) == distance:
                count += 1
            return

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_row = i + dr
            next_col = j + dc
            if not (0 <= next_row < m and 0 <= next_col < n) or (next_row, next_col) in walked or (
            next_row, next_col) in obstacles:
                continue

            walked.add((next_row, next_col))
            backtrack(m, n, next_row, next_col)
            walked.remove((next_row, next_col))

    backtrack(m, n, start[0], start[1])

    return count