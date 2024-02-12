class Solution:
    def get_max_height(self, height: list[int]) -> list[int]:
        max_height = 0
        result = []
        for value in height:
            max_height = max(max_height, value)
            result.append(max(max_height, value))
        return result

    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        left_max = self.get_max_height(height)
        right_max = self.get_max_height(height[::-1])[::-1]
        start, end = 0, len(height) - 1
        result = 0
        while start < end:
            if left_max[start] < right_max[end]:
                result += max(min(left_max[start], right_max[end]) - height[start], 0)
                start += 1
            else:
                result += max(min(left_max[start], right_max[end]) - height[end], 0)
                end -= 1
        return result


def main():
    answer = Solution()
    assert answer.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert answer.trap([4, 2, 0, 3, 2, 5]) == 9
    assert answer.trap([4, 2, 3]) == 1
    assert answer.trap([4, 2, 3, 1]) == 1
    assert answer.trap([4, 2, 3, 1, 2]) == 2
    assert answer.trap([4, 2, 3, 1, 2, 1]) == 2
    assert answer.trap([4, 2, 3, 1, 2, 1, 3]) == 6
    assert answer.trap([4, 2, 3, 1, 2, 1, 3, 1]) == 6
    assert answer.trap([4, 2, 3, 1, 2, 1, 3, 1, 3]) == 8
    print("All test cases passed.")


if __name__ == "__main__":
    main()
