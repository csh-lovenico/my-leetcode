class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = []
        self.path = []

        def dfs(root: 'TreeNode', target: 'TreeNode'):
            if root is None:
                return
            else:
                stack.append(root)
                if root.val == target.val:
                    self.path = stack.copy()
                else:
                    dfs(root.left, target)
                    dfs(root.right, target)
                stack.pop()

        dfs(root, p)
        p_path = self.path.copy()
        self.path.clear()
        dfs(root, q)
        q_path = self.path.copy()

        for i in range(min(len(p_path), len(q_path)) - 1, -1, -1):
            if p_path[i].val == q_path[i].val:
                return p_path[i]

        return None
