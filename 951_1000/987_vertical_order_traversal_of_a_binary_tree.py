# Definition for a binary tree node.
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        hashmap = collections.defaultdict(list)

        def dfs(rt: Optional[TreeNode], row: int, col: int):
            nonlocal hashmap
            if not rt:
                return
            hashmap[col].append((row, rt.val))
            dfs(rt.left, row + 1, col - 1)
            dfs(rt.right, row + 1, col + 1)

        dfs(root, 0, 0)
        k = sorted(list(hashmap.keys()))
        for n in k:
            result.append([i[1] for i in sorted(hashmap[n])])
        return result


if __name__ == '__main__':
    print(sorted([3, 2, 2]))
