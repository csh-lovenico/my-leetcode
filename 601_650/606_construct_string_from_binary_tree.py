# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = ''

        def dfs(rt: Optional[TreeNode]):
            nonlocal result
            result += '('
            if rt:
                result += str(rt.val)
                if (rt.left and rt.right) or (not rt.left and rt.right):
                    dfs(rt.left)
                    dfs(rt.right)
                elif rt.left and not rt.right:
                    dfs(rt.left)
            result += ')'
            return

        dfs(root)
        return result[1:-1]
