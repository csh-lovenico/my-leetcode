# Definition for a binary tree node.


# https://leetcode.com/problems/symmetric-tree/discuss/2423766/Easy-oror-0-ms-100-(Fully-Explained)(Java-C%2B%2B-Python-JS-Python3)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root):
        # Special case...
        if not root:
            return True
        # Return the function recursively...
        return self.isSame(root.left, root.right)

    # A tree is called symmetric if the left subtree must be a mirror reflection of the right subtree...
    def isSame(self, left_root: TreeNode, right_root: TreeNode) -> bool:
        # If both root nodes are null pointers, return true...
        if left_root is None and right_root is None:
            return True
        # If exactly one of them is a null node, return false...
        if left_root is None or right_root is None:
            return False
        # If root nodes haven't same value, return false...
        if left_root.val != right_root.val:
            return False
        # Return true if the values of root nodes are same and left as well as right subtrees are symmetric...
        return self.isSame(left_root.left, right_root.right) and self.isSame(left_root.right, right_root.left)
