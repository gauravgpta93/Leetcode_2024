# Create a dataclass for a doubly linked list node
from dataclasses import dataclass


@dataclass
class ListNode:
    key: int
    value: int
    prev: "ListNode" = None
    next: "ListNode" = None


class LRUCache:

    def __init__(self, capacity: int):
        self.max_capacity:int = capacity
        self.cache: dict[int, ListNode] = {}
        self.start: ListNode | None = None
        self.end: ListNode | None = None

    def _update_node_to_end(self, node: ListNode) -> None:
        if node == self.end:
            return
        if node == self.start:
            self.start = self.start.next
            self.start.prev = None
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        self.end.next = node
        node.prev = self.end
        node.next = None
        self.end = node

    def _update_value(self, key: int, value: int) -> None:
        node = self.cache[key]
        node.value = value
        self._update_node_to_end(node)

    def _remove_start(self) -> None:
        if self.start == self.end:
            self.start = self.end = None
        else:
            self.start = self.start.next
            self.start.prev = None

    def _add_to_end(self, key: int, value: int) -> None:
        node = ListNode(key, value)
        if not self.start:
            self.start = self.end = node
        else:
            self.end.next = node
            node.prev = self.end
            self.end = node
        self.cache[key] = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self._update_node_to_end(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._update_value(key, value)
        else:
            self._add_to_end(key, value)
            if len(self.cache) > self.max_capacity:
                del self.cache[self.start.key]
                self._remove_start()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

def main():
    ans = LRUCache(2)
    ans.put(1, 1)
    ans.put(2, 2)
    assert (output := ans.get(1)) == 1, output
    ans.put(3, 3)
    assert (output := ans.get(2)) == -1, output
    ans.put(4, 4)
    assert (output := ans.get(1)) == -1, output
    assert (output := ans.get(3)) == 3, output
    assert (output := ans.get(4)) == 4, output

    print("Passed all test cases!")

if __name__ == "__main__":
    main()