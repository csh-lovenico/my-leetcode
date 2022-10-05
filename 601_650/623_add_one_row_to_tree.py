# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new = TreeNode(val)
            new.left = root
            return new
        queue = collections.deque()
        queue.append((root, 1))
        while queue:
            curr_d = queue[0][1]
            if curr_d == depth - 1:
                break
            node, d = queue.popleft()
            if not node:
                continue
            queue.append((node.left, d + 1))
            queue.append((node.right, d + 1))

        for n, _ in queue:
            if not n:
                continue
            left = n.left
            right = n.right
            n_left = TreeNode(val)
            n_right = TreeNode(val)
            n_left.left = left
            n_right.right = right
            n.left = n_left
            n.right = n_right
        return root


