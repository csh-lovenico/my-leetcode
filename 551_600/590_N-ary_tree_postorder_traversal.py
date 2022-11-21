from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children:List['Node']=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def dfs(rt: 'Node'):
            if not rt:
                return

            for child in rt.children:
                dfs(child)

            res.append(rt.val)

        dfs(root)
        return res
