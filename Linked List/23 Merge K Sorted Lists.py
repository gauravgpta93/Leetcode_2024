# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # This can be replaced by heapq for O(log k) time complexity
    def find_min(self, lists: list[ListNode]) -> tuple[ListNode, list[ListNode]]:
        if not lists:
            return None, []
        max_node: tuple[ListNode, int] = (lists[0], 0)
        for i in range(1, len(lists)):
            if lists[i].val < max_node[0].val:
                max_node = (lists[i], i)
        if lists[max_node[1]].next:
            lists[max_node[1]] = lists[max_node[1]].next
        else:
            lists.pop(max_node[1])
        return max_node[0], lists

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        start = current = ListNode()
        value_list_nodes: list[ListNode] = []
        for list_node in lists:
            if list_node:
                value_list_nodes.append(list_node)
        while value_list_nodes:
            max_node, value_list_nodes = self.find_min(value_list_nodes)
            current.next = max_node
            current = current.next
        return start.next