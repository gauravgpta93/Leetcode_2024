# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        first, second = list1, list2
        current = start = ListNode()
        while first and second:
            if first.val < second.val:
                current.next = first
                first = first.next
            else:
                current.next = second
                second = second.next
            current = current.next

        current.next = first or second
        return start.next

