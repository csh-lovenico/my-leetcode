# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root or not p:
            return None

        val_list = []
        node_list = []

        def dfs(rt: Optional[TreeNode]):
            if not rt:
                return
            nonlocal val_list
            dfs(rt.left)
            val_list.append(rt.val)
            node_list.append(rt)
            dfs(rt.right)

        dfs(root)

        idx = val_list.index(p.val)
        if idx == len(val_list) - 1:
            return None
        else:
            return node_list[idx + 1]
