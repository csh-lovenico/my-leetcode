# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # let p < q
        if p.val > q.val:
            temp = p
            p = q
            q = temp

        # Search left child if p and q < root
        # Search right child if p and q > root
        # Return root if p < root and q > root, or p = root or q = root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if p.val == root.val or q.val == root.val:
            return root
        if p.val < root.val < q.val:
            return root
