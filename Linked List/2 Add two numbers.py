# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ans = current = ListNode(0)
        while l1 or l2 or carry:
            current_value = carry
            current_value += l1.val if l1 else 0
            current_value += l2.val if l2 else 0
            carry = current_value // 10
            current.next = ListNode(current_value % 10)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return ans.next