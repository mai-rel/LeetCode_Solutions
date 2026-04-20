from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False

    result = False

    def dfs(node, total=0):
        nonlocal result
        total += node.val

        if result:
            return

        if not node.left and not node.right:
            if total == targetSum:
                result = True
                return

        if node.left:
            dfs(node.left, total)
        if node.right:
            dfs(node.right, total)

    dfs(root)
    return result




