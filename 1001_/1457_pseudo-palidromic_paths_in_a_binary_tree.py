# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        result = 0
        init = set()

        def dfs(rt: Optional[TreeNode], curr: set):
            nonlocal result
            if rt.val in curr:
                curr.remove(rt.val)
            else:
                curr.add(rt.val)
            if not rt.left and not rt.right:
                if len(curr) <= 1:
                    result += 1
            if rt.left:
                dfs(rt.left, curr.copy())
            if rt.right:
                dfs(rt.right, curr.copy())

        dfs(root, init)
        return result

# optimized way
# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/discuss/2573851/Short-oror-C%2B%2B-oror-Java-oror-PYTHON-oror-Explained-Solution-oror-Beginner-Friendly-oror-BY-MR-CODER
# using a global variable may reduce time and memory
