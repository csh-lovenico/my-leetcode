# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.serialize(p) == self.serialize(q)

    def serialize(self, root: Optional['TreeNode']) -> str:
        if root is None:
            return ""
        result = []
        queue = []
        result.append(str(root.val))
        queue.append([root.left, 1])
        queue.append([root.right, 1])
        current_depth = 1
        current_result = []
        while len(queue) > 0:
            head = queue.pop(0)
            if head[0] is None:
                current_result.append("null")
                continue
            if head[1] > current_depth:
                result.extend(current_result)
                current_result = []
                current_depth = head[1]
            current_result.append(str(head[0].val))
            queue.append([head[0].left, head[1] + 1])
            queue.append([head[0].right, head[1] + 1])

        if len(current_result) > 0:
            result.extend(current_result)
        return ','.join(result)
