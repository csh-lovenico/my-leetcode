# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/count-complete-tree-nodes/solutions/62065/two-python-solutions-recursive-and-iterative-o-logn-2/
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def get_height(node):
            count = 0
            while node:
                count += 1
                node = node.left
            return count

        ans = 0
        while root:
            left = get_height(root.left)
            if left == get_height(root.right):
                ans += (1 << left)
                root = root.right
            else:
                ans += (1 << (left - 1))
                root = root.left
        return ans
