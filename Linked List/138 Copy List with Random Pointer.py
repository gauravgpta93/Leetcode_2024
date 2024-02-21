# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def create_dupliacte_nodes(self, head: "Optional[Node]") -> None:
        current = head
        while current:
            duplicate = Node(current.val, current.next, current.random)
            current.next = duplicate
            current = duplicate.next

    def update_random_pointers(self, head: "Optional[Node]") -> None:
        current = head.next
        while current:
            if current.random:
                current.random = current.random.next
            current = current.next.next if current.next else None

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None
        self.create_dupliacte_nodes(head)
        self.update_random_pointers(head)
        ans = head.next
        current = head
        while current and current.next:
            temp = current.next
            current.next = temp.next
            current = temp

        return ans
