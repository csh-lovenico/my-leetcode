# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ans = 0

        def dfs(rt: Optional[TreeNode], curr: int):
            nonlocal ans
            if not rt:
                return
            curr += rt.val
            if (not rt.left) and (not rt.right):
                if curr == targetSum:
                    ans += 1
            else:
                if rt.left:
                    dfs(rt.left, curr)
                if rt.right:
                    dfs(rt.right, curr)

        dfs(root, 0)
        return ans > 0
