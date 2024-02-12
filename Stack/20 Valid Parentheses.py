class Solution:
    def isValid(self, s: str) -> bool:
        seen: list[str] = []
        close_open_map: dict[str, str] = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        for bracket in s:
            if bracket in close_open_map:
                if not seen or seen.pop() != close_open_map[bracket]:
                    return False
            else:
                seen.append(bracket)
        return False if seen else True  # if seen is empty, return True, else return False


def main():
    answer = Solution()
    assert answer.isValid("()") is True
    assert answer.isValid("()[]{}") is True
    assert answer.isValid("(]") is False
    assert answer.isValid("([)]") is False
    assert answer.isValid("{[]}") is True
    assert answer.isValid("]") is False
    assert answer.isValid("") is True
    print("All test cases passed.")


if __name__ == "__main__":
    main()
