# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/2472358/Pythonor-DFSor-Recursive-or-Easy-to-understand-orWithout-DP-or-Less-space-than-DP
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dm = float('-inf')

        def dfs(node):
            if not node:
                return 0

            leftval = dfs(node.left)
            rightval = dfs(node.right)

            # compare: current max value, left+root, right+root, left+right+root, root itself
            self.dm = max(self.dm, leftval + node.val, rightval + node.val, leftval + rightval + node.val, node.val)
        
            return max(leftval + node.val, rightval + node.val, node.val)

        dfs(root)
        return int(self.dm)

