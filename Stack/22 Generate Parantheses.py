class Solution:
    def create_valid_parenthesis(
        self,
        total: int,
        open_count: int,
        close_count: int,
        current: str,
        result: list[str],
    ):
        result_list = []
        if len(current) == total * 2:
            # result.append(current)
            return [current]
        if open_count < total:
            result_list.extend(
                self.create_valid_parenthesis(
                    total, open_count + 1, close_count, current + "(", result
                )
            )
        if close_count < open_count:
            result_list.extend(
                self.create_valid_parenthesis(
                    total, open_count, close_count + 1, current + ")", result
                )
            )
        return result_list

    # def generateParenthesis(self, n: int) -> list[str]:
    #     result = []
    #     return self.create_valid_parenthesis(n, 0, 0, "", result)
        # return result

    # Try with Stack
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        stack = []
        stack.append(("", 0, 0))
        while stack:
            current, open_count, close_count = stack.pop()
            if len(current) == n * 2:
                result.append(current)
            if open_count < n:
                stack.append((current + "(", open_count + 1, close_count))
            if close_count < open_count:
                stack.append((current + ")", open_count, close_count + 1))
        return result
def main():
    answer = Solution()
    assert set(answer.generateParenthesis(3)) == {
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()",
    }
    assert answer.generateParenthesis(1) == ["()"]
    print("All test cases passed.")


if __name__ == "__main__":
    main()
