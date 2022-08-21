# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/maximum-width-of-binary-tree/discuss/2450764/Python-BFS-O(n)-solution
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([[root, 0]])  # [root, index]

        maxdif = 0

        while q:
            curdif = 0
            size = len(q)

            # leftmost in the level
            nodeleft, leftidx = q[0]
            # righmost in the level
            noderight, rightidx = q[size - 1]
            # get the difference
            lvldif = rightidx - leftidx

            # update max
            if lvldif > maxdif:
                maxdif = lvldif

            for i in range(len(q)):
                node, idx = q.popleft()
                if node.left:
                    q.append([node.left, 2 * idx])
                if node.right:
                    q.append([node.right, 2 * idx + 1])

        return maxdif + 1
