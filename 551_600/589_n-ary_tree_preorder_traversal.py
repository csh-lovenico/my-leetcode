from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val: int = None, children: List['Node'] = None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []

        def dfs(rt: 'Node'):
            nonlocal result
            if not rt:
                return
            result.append(rt.val)
            for child in rt.children:
                dfs(child)

        dfs(root)

        return result
