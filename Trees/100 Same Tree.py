# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    # Iterative
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     node_queue = deque([(p, q)])
    #     while node_queue:
    #         node_1, node_2 = node_queue.popleft()
    #         if not node_1 and not node_2:
    #             continue
    #         if not node_1 or not node_2:
    #             return False
    #         if node_1.val != node_2.val:
    #             return False
    #         node_queue.append((node_1.left, node_2.left))
    #         node_queue.append((node_1.right, node_2.right))
    #     return True

    # Recursive
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)