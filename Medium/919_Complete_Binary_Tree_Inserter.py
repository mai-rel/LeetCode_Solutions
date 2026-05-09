from typing import Optional
from collections import deque


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.queue = deque([self.root])
        self.node = self.queue.popleft()

        while self.node.left and self.node.right:
            self.queue.append(self.node.left)
            self.queue.append(self.node.right)
            self.node = self.queue.popleft()

        if self.node.left:
            self.queue.append(self.node.left)

    def insert(self, val: int) -> int:
        new_node = TreeNode(val)
        parent_val = self.node.val

        if not self.node.left:
            self.node.left = new_node
            self.queue.append(new_node)

        elif not self.node.right:
            self.node.right = new_node
            self.queue.append(new_node)
            self.node = self.queue.popleft()

        return parent_val

    def get_root(self) -> Optional[TreeNode]:
        return self.root
