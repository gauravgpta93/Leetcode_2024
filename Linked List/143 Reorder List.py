# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def get_mid_point(self, head: ListNode | None) -> ListNode | None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head: ListNode | None) -> ListNode | None:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        mid = self.get_mid_point(head)
        second_half = self.reverse(mid.next)
        mid.next = None

        first_half = head
        while second_half:
            temp_first = first_half.next
            temp_second = second_half.next
            first_half.next = second_half
            second_half.next = temp_first
            first_half = temp_first
            second_half = temp_second
        return
