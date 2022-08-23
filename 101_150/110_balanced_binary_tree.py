from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left is None:
            l_depth = 0
        else:
            l_depth = self.findDepth(root.left, 1)
        if root.right is None:
            r_depth = 0
        else:
            r_depth = self.findDepth(root.right, 1)
        return l_depth != -1 and r_depth != -1 and abs(l_depth - r_depth) <= 1

    def findDepth(self, root: Optional[TreeNode], depth: int) -> int:
        if root is None:
            return depth - 1
        else:
            l_depth = self.findDepth(root.left, depth + 1)
            r_depth = self.findDepth(root.right, depth + 1)
            if abs(l_depth - r_depth) <= 1 and l_depth > 0 and r_depth > 0:
                return max(l_depth, r_depth)
            else:
                return -1


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left.left=TreeNode(4)
    root.left.left.right = TreeNode(4)
    print(Solution().isBalanced(root))
