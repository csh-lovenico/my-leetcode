from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        def dfs(rt: Optional[TreeNode], isLeft: bool) -> int:
            if not rt:
                return 0
            if isLeft and (not rt.left) and (not rt.right):
                return rt.val + dfs(rt.left, True) + dfs(rt.right, False)
            else:
                return dfs(rt.left, True) + dfs(rt.right, False)

        return dfs(root, False)
