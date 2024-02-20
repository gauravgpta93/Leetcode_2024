# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        temp, current = None, head
        while current:
            next_node = current.next
            current.next = temp
            temp = current
            current = next_node

        return temp