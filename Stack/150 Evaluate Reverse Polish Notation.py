class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        result: list[int] = []
        for token in tokens:
            if token in "+-*/":
                right = result.pop()
                left = result.pop()
                if token == "+":
                    result.append(left + right)
                elif token == "-":
                    result.append(left - right)
                elif token == "*":
                    result.append(left * right)
                else:
                    result.append(int(left / right))
            else:
                result.append(int(token))
        return result[0]


def main():
    answer = Solution()
    assert answer.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert answer.evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert (
        answer.evalRPN(
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        )
        == 22
    ), answer.evalRPN(
        ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    )

    print("All test cases passed.")


if __name__ == "__main__":
    main()
