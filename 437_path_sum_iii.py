# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/path-sum-iii/discuss/2404673/Python-C%2B%2B-Easy-solution-faster-than-95-using-hashmap
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt = 0
        hm = defaultdict(int)
        hm[0] += 1

        # Similar to 560: Subarray sum equals K
        def traverse(node, currSum):
            nonlocal cnt
            if not node:
                return
            currSum += node.val

            cnt += hm[currSum - targetSum]
            hm[currSum] += 1
            traverse(node.left, currSum)
            traverse(node.right, currSum)
            hm[currSum] -= 1

        traverse(root, 0)
        return cnt
