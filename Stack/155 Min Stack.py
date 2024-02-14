class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack: list[int] = []
        self.min_stack: list[int] = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # add to min stack every time
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


def main():
    answer = MinStack()
    answer.push(-2)
    answer.push(0)
    answer.push(-3)
    assert answer.getMin() == -3
    answer.pop()
    assert answer.top() == 0
    assert answer.getMin() == -2
    print("All test cases passed.")


if __name__ == "__main__":
    main()
