import collections
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val: int = None, children: List['Node'] = None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        queue = collections.deque()
        queue.append((root, 0))
        result = []
        cur_result = []
        last_depth = 0
        while queue:
            node, depth = queue.popleft()
            if not node:
                continue
            if depth != last_depth:
                result.append(cur_result)
                cur_result.clear()
                last_depth = depth
            cur_result.append(node.val)
            for child in node.children:
                queue.append((child, depth + 1))

        if len(cur_result) > 0:
            result.append(cur_result)
        return result
