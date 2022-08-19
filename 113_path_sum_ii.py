# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(root: Optional[TreeNode], visited: List[int]):
            if root is None:
                return
            visited.append(root.val)
            if sum(visited) == targetSum and root.left is None and root.right is None:
                result.append(visited.copy())
                return
            else:
                dfs(root.left, visited.copy())
                dfs(root.right, visited.copy())

        dfs(root, [])
        return result
