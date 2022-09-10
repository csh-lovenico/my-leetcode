import collections
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        queue = collections.deque()
        curr: Optional['Node'] = None
        prev: Optional['Node'] = None
        cur_depth = -1
        queue.append((root, 0))
        while queue:
            node, depth = queue.popleft()
            if not node:
                continue
            if depth > cur_depth:
                curr = node
                cur_depth = depth
                prev = None
            else:
                curr = node
                if prev:
                    prev.next = curr
            prev = curr
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))

        return root
