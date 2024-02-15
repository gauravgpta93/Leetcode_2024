class Solution:
    def calPoints(self, operations: list[str]) -> int:
        result = []
        for op in operations:
            if op == "+":
                result.append(result[-1] + result[-2])
            elif op == "D":
                result.append(result[-1] * 2)
            elif op == "C":
                result.pop()
            else:
                result.append(int(op))
        return sum(result)


def main():
    operations = ["5", "2", "C", "D", "+"]
    assert (result := Solution().calPoints(operations)) == 30, f"unexpected {result=}"
    assert (
        result := Solution().calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"])
    ) == 27, f"unexpected {result=}"

    print("All test cases passed!")


if __name__ == "__main__":
    main()
