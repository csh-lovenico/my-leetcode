# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(rt: Optional[TreeNode]):
            nonlocal result
            if not rt:
                return
            dfs(rt.left)
            result.append(rt.val)
            dfs(rt.right)
        dfs(root)
        return result
