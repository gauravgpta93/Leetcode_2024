# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def find_kth_node(self, head: ListNode, k: int) -> ListNode:
    #     while k > 1 and head:
    #         head = head.next
    #         k -= 1
    #     return head
    #
    # def reverse_list(self, start: ListNode, end: ListNode, prev: ListNode | None):
    #     if not start or not end:
    #         return
    #     current = start
    #     forward = end.next
    #     temp_prev = prev
    #     while current != forward:
    #         temp = current.next
    #         current.next = temp_prev
    #         temp_prev = current
    #         current = temp
    #     prev.next = end
    #     start.next = forward
    #
    # def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    #     if k == 1 or not head:
    #         return head
    #     start = head
    #     ans = end = self.find_kth_node(head, k)
    #     prev = ListNode(next=head)
    #     while end:
    #         self.reverse_list(start, end, prev)
    #         prev = start
    #         start = start.next
    #         end = self.find_kth_node(start, k)
    #     return ans if ans else head

    # simple recursive solution
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        # check if enough left
        for _ in range(k):
            if not current:
                return head
            current = current.next

        # reverse till k
        prev = None
        current = head
        for _ in range(k):
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        head.next = self.reverseKGroup(current, k)
        return prev