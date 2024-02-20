# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)
        nth_node = head
        for _ in range(n):
            nth_node = nth_node.next

        current = dummy
        while nth_node.next:
            nth_node = nth_node.next
            current = current.next

        current.next = current.next.next
        return dummy.next