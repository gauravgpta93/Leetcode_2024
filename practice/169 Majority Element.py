class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        current_count: int = 0
        current_value: int | None = None
        for value in nums:
            if current_count == 0:
                current_value = value
            current_count += 1 if value == current_value else -1

        return current_value


def main():
    answer = Solution()
    assert answer.majorityElement([3, 2, 3]) == 3
    assert answer.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    print("All test cases passed.")


if __name__ == "__main__":
    main()
