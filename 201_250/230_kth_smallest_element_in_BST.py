# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return None
        result = []

        def in_order_traversal(root: Optional[TreeNode]):
            if root is None:
                return
            in_order_traversal(root.left)
            result.append(root.val)
            in_order_traversal(root.right)

        in_order_traversal(root)
        return result[k-1]
