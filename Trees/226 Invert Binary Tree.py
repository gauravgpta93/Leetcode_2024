# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     if not root:
    #         return None
    #     # root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    #     temp_left = root.left
    #     temp_right = root.right
    #     root.left = self.invertTree(temp_right)
    #     root.right = self.invertTree(temp_left)
    #     return root

    # Using iterative approach (BFS traversal using queue)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        while queue:
            temp = queue.popleft()
            # swap the left and right children
            temp.left, temp.right = temp.right, temp.left
            # add to the queue the left and right children
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return root