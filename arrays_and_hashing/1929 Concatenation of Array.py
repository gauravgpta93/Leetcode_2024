class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        return nums + nums  # since the list is of immumate objects, new list is created and returned


def main():
    assert Solution().getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
    assert Solution().getConcatenation([1]) == [1, 1]
    assert Solution().getConcatenation([1, 2, 3, 4]) == [1, 2, 3, 4, 1, 2, 3, 4]
    print('All test cases passed!')


if __name__ == '__main__':
    main()
