# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None:
            l_depth = 0
        else:
            l_depth = self.findDepth(root.left, 1)
        if root.right is None:
            r_depth = 0
        else:
            r_depth = self.findDepth(root.right, 1)
        # similar to diameter of binary tree and balanced binary tree
        # +1 to calculate the number of nodes
        return max(l_depth, r_depth) + 1

    def findDepth(self, root: Optional[TreeNode], depth: int) -> int:
        # similar to diameter of binary tree
        if root is None:
            return depth - 1
        else:
            l_depth = self.findDepth(root.left, depth + 1)
            r_depth = self.findDepth(root.right, depth + 1)
            return max(l_depth, r_depth)
