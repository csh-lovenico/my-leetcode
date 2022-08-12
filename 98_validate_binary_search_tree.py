# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.stack = []
        # direction: 0: left 1:right
        self.direction_stack = []

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        self.stack.append(root.val)
        return self.dfs(root.left, 0) and self.dfs(root.right, 1)

    def dfs(self, root: Optional[TreeNode], direction: int):
        self.direction_stack.append(direction)
        if root is None:
            self.direction_stack.pop()
            return True
        self.stack.append(root.val)
        result = True
        for i in range(len(self.direction_stack)):
            # left: less than
            if self.direction_stack[i] == 0:
                result = result and root.val < self.stack[i]
                if not result:
                    break
            # right: greater than
            elif self.direction_stack[i] == 1:
                result = result and root.val > self.stack[i]
                if not result:
                    break
        dfs_result = self.dfs(root.left, 0) and self.dfs(root.right, 1)
        self.direction_stack.pop()
        self.stack.pop()
        return result and dfs_result
