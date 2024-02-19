class Solution:
    # def check_lower(self, nums: list[int], target: int, mid: int) -> bool:
    #     return nums[mid] < target
    #
    # def searchInsert(self, nums: list[int], target: int) -> int:
    #     left, right = 0, len(nums) - 1
    #     while left < right:
    #         mid = (left + right) // 2
    #         if self.check_lower(nums, target, mid):
    #             left = mid + 1
    #         else:
    #             right = mid
    #     return left if nums[left] >= target else left + 1

    # Solving through lower bound
    def check_target_higher(self, nums: list[int], target: int, mid: int) -> bool:
        return nums[mid] >= target

    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if self.check_target_higher(nums, target, mid):
                right = mid
            else:
                left = mid + 1
        return left
def main():
    answer = Solution()
    assert (output := answer.searchInsert([1, 3, 5, 6], 5)) == 2, f"output: {output}"
    assert (output := answer.searchInsert([1, 3, 5, 6], 2)) == 1, f"output: {output}"
    assert (output := answer.searchInsert([1, 3, 5, 6], 7)) == 4, f"output: {output}"
    assert (output := answer.searchInsert([1, 3, 5, 6], 0)) == 0, f"output: {output}"
    assert (output := answer.searchInsert([1], 0)) == 0, f"output: {output}"

    print("Passed all test cases!")

if __name__ == '__main__':
    main()