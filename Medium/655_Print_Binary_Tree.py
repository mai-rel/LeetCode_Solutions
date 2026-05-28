from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_height(node):
    if not node:
        return 0
    if not node.left and not node.right:
        return 1

    left_h = get_height(node.left)
    right_h = get_height(node.right)
    return max(left_h, right_h) + 1


def printTree(root: Optional[TreeNode]) -> List[List[str]]:
    height = get_height(root) - 1

    rows = height + 1
    cols = 2 ** (height + 1) - 1
    matrix = [[''] * cols for _ in range(rows)]

    root_row = 0
    root_col = (cols - 1) // 2
    matrix[root_row][root_col] = str(root.val)

    def dfs(node, row, col, height):
        new_row = row + 1

        if node.left:
            value = str(node.left.val)
            col_for_left = col - 2 ** (height - row - 1)
            matrix[new_row][col_for_left] = value
            dfs(node.left, new_row, col_for_left, height)

        if node.right:
            value = str(node.right.val)
            col_for_right = col + 2 ** (height - row - 1)
            matrix[new_row][col_for_right] = value
            dfs(node.right, new_row, col_for_right, height)

    dfs(root, root_row, root_col, height)
    return matrix