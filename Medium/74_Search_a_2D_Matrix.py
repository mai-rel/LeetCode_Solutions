from typing import List


def get_row(grid, target):
    l = 0
    r = len(grid) - 1

    while l < r:
        m = (l + r + 1) // 2
        if target < grid[m][0]:
            r = m - 1
        else:
            l = m

    return l


def get_col(row, target):
    l = 0
    r = len(row) - 1

    while l < r:
        m = (l + r + 1) // 2
        if target < row[m]:
            r = m - 1
        else:
            l = m

    return l


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    row = get_row(matrix, target)

    if target < matrix[row][0] or target > matrix[row][-1]:
        return False

    col = get_col(matrix[row], target)

    if matrix[row][col] == target:
        return True
    return False