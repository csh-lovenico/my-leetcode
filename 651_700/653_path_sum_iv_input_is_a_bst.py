# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/discuss/2683496/Easy-to-understand-BFS-and-DFS-solutions-98
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        que = [root]
        # initialize que
        h = set()
        while que:
            node = que.pop(0)
            # pop the first node
            if node:
                if node.val in h:
                    return True
                else:
                    h.add(k-node.val)
                    if node.right:
                        que.append(node.right)
                    if node.left:
                        que.append(node.left)
        return False
