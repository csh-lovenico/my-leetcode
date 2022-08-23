from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# bfs
# https://leetcode.com/problems/subtree-of-another-tree/discuss/2409507/Simple-Solution-oror-Python-oror-Easily-Understood-oror-iterative-and-recursive
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if root.val == subRoot.val:
            q = []
            q.append((root.left, subRoot.left))
            q.append((root.right, subRoot.right))

            all_match = True
            while all_match and len(q):
                (r, s) = q.pop()
                if not s and not r:
                    continue
                elif not s or not r or r.val != s.val:
                    all_match = False
                else:
                    q.append((r.left, s.left))
                    q.append((r.right, s.right))

            if all_match:
                return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
# dfs also in this solution
