class Solution:
    # Cannot be done preserving order of elements in place
    # def sort_array_by_sign(self, nums: list[int]):
    #     iterator = 0
    #     for index, num in enumerate(nums):
    #         if num < 0:
    #             iterator = index
    #             break
    #     negative_pointer = iterator
    #     positive_pointer = iterator + 1
    #     while positive_pointer < len(nums):
    #         nums[negative_pointer], nums[positive_pointer] = (
    #             nums[positive_pointer],
    #             nums[negative_pointer],
    #         )
    #         if nums[negative_pointer] < 0:
    #             negative_pointer += 1
    #
    #         positive_pointer += 1
    #     return nums

    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums)
        positive_pointer = 0
        negative_pointer = 1
        for num in nums:
            if num < 0:
                ans[negative_pointer] = num
                negative_pointer += 2
            else:
                ans[positive_pointer] = num
                positive_pointer += 2

        return ans


def main():
    sol = Solution()
    # assert (result := sol.sort_array_by_sign([3, 1, -2, -5, 2, -4])) == [
    #     2,
    #     1,
    #     2,
    #     -2,
    #     -5,
    #     -4,
    # ], f"expected {result=}"
    assert (result := sol.rearrangeArray([3, 1, -2, -5, 2, -4])) == [
        3,
        -2,
        1,
        -5,
        2,
        -4,
    ], f"expected {result=}"
    assert (result := sol.rearrangeArray([-1, 1])) == [1, -1], f"expected {result=}"


if __name__ == "__main__":
    main()
