# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        root_index = len(nums) // 2
        root = TreeNode(nums[root_index])
        root.left = self.sortedArrayToBST(nums[0:root_index])
        root.right = self.sortedArrayToBST(nums[root_index + 1:])
        return root
