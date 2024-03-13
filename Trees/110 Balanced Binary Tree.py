# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    _check_balanced: bool = True

    def max_depth(self, root):
        if not root.left and not root.right:
            return 1
        left_depth = self.max_depth(root.left) if root.left else 0
        right_depth = self.max_depth(root.right) if root.right else 0
        if abs(left_depth - right_depth) > 1:
            self._check_balanced = False
        return max(left_depth, right_depth) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.max_depth(root)
        return self._check_balanced
