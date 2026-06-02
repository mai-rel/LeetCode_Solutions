from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])

        self.prefixSums = [[0] * (n + 1) for _ in range(m + 1)]

        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                self.prefixSums[i + 1][j + 1] = self.prefixSums[i + 1][j] + self.prefixSums[i][j + 1] - \
                                                self.prefixSums[i][j] + value

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefixSums[row2 + 1][col2 + 1] - self.prefixSums[row1][col2 + 1] - self.prefixSums[row2 + 1][col1] + \
               self.prefixSums[row1][col1]