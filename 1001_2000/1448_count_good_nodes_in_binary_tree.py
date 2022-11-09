# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        def dfs(rt: TreeNode, cur_max: int):
            nonlocal result
            if not rt:
                return
            if rt.val >= cur_max:
                result += 1
                dfs(rt.left, rt.val)
                dfs(rt.right, rt.val)
            else:
                dfs(rt.left, cur_max)
                dfs(rt.right, cur_max)

        dfs(root, -(10 ** 5))
        return result
