class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        for index, height in enumerate(heights):
            while stack and stack[-1][0] > height:
                stack_height, stack_index = stack.pop()
                stack_area = stack_height * (index - stack[-1][1] - 1) if stack else stack_height * index
                max_area = max(max_area, stack_area)
            stack.append((height, index))
        return max_area


def main():
    ans = Solution()
    assert (output := ans.largestRectangleArea([2, 1, 5, 6, 2, 3])) == 10, output
    assert (output := ans.largestRectangleArea([2, 4])) == 4, output
    assert (output := ans.largestRectangleArea([2, 1, 2])) == 3, output

    print("Passed all tests!")


if __name__ == "__main__":
    main()
