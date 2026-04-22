from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False

    targetSum -= root.val
    if not root.left and not root.right:
        if targetSum == 0:
            return True

    return hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum)




