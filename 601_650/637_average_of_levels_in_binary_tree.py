# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        result = []
        queue = []
        result.append(root.val)
        queue.append([root.left, 1])
        queue.append([root.right, 1])
        current_depth = 1
        current_result = []
        while len(queue) > 0:
            head = queue.pop(0)
            if head[0] is None:
                continue
            if head[1] > current_depth:
                result.append(sum(current_result)/len(current_result))
                current_result = []
                current_depth = head[1]
            current_result.append(head[0].val)
            queue.append([head[0].left, head[1] + 1])
            queue.append([head[0].right, head[1] + 1])

        if len(current_result) > 0:
            result.append(sum(current_result)/len(current_result))
        return result
