# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/largest-bst-subtree/discuss/1992484/My-python-O(N)-simple-solution
# https://leetcode.com/problems/largest-bst-subtree/discuss/78895/Short-Python-solution

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def find(node):
            if not node:
                return float('inf'), float('-inf'), 0
            lmin, lmax, lnum = find(node.left)
            rmin, rmax, rnum = find(node.right)
            n = float('-inf')
            if lmax < node.val < rmin:
                n = lnum + rnum + 1
                self.res = max(n, self.res)
            return min(node.val, lmin), max(node.val, rmax), n

        find(root)
        return self.res
