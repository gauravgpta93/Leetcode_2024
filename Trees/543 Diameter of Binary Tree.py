# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_seen: set[int] = set()
        self.max_depth(root, max_seen)
        return max(max_seen)

    def max_depth(self, node, max_seen: set[int]) -> int:
        if not node.left and not node.right:
            max_seen.add(0)
            return 1
        left_depth = self.max_depth(node.left, max_seen) if node.left else 0
        right_depth = self.max_depth(node.right, max_seen) if node.right else 0
        max_seen.add(left_depth + right_depth)
        return max(left_depth, right_depth) + 1
