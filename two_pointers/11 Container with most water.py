class Solution:
    def maxArea(self, height: list[int]) -> int:
        start_index, end_index = 0, len(height) - 1
        max_hold = 0
        while start_index < end_index:
            start_height, end_height = height[start_index], height[end_index]
            max_hold = max(
                max_hold, min(start_height, end_height) * (end_index - start_index)
            )
            if start_height < end_height:
                start_index += 1
            else:
                end_index -= 1
        return max_hold


def main():
    answer = Solution()
    assert answer.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert answer.maxArea([1, 1]) == 1
    assert answer.maxArea([4, 3, 2, 1, 4]) == 16
    assert answer.maxArea([1, 2, 1]) == 2
    print("All test cases passed.")


if __name__ == "__main__":
    main()
