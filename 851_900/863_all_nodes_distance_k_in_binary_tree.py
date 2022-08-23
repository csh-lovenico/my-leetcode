# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph_dict = collections.defaultdict(list)
        queue = collections.deque()
        queue.append((root.val, root.left))
        queue.append((root.val, root.right))
        visited = set()
        result = []
        while queue:
            parent_val, child = queue.popleft()
            if not child:
                continue
            graph_dict[parent_val].append(child.val)
            graph_dict[child.val].append(parent_val)
            queue.append((child.val, child.left))
            queue.append((child.val, child.right))

        queue.append((target.val, 0))
        while queue:
            head = queue.popleft()
            if head[0] in visited:
                continue
            if head[1] > k:
                continue
            if head[1] == k:
                result.append(head[0])
                continue
            visited.add(head[0])
            for item in graph_dict[head[0]]:
                queue.append((item, head[0] + 1))
        return result
