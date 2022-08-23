# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        queue = []
        result.append([root.val])
        queue.append([root.left, 1])
        queue.append([root.right, 1])
        current_depth = 1
        current_result = []
        while len(queue) > 0:
            head = queue.pop(0)
            if head[0] is None:
                continue
            if head[1] > current_depth:
                # current depth is the last depth
                if current_depth % 2 != 0:
                    current_result.reverse()
                result.append(current_result)
                current_result = []
                current_depth = head[1]
            current_result.append(head[0].val)
            queue.append([head[0].left, head[1] + 1])
            queue.append([head[0].right, head[1] + 1])

        if len(current_result) > 0:
            if current_depth % 2 != 0:
                current_result.reverse()
            result.append(current_result)
        return result
