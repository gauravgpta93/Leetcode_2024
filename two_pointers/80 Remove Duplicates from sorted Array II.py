class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        start_pointer, end_pointer = 1, 1
        while end_pointer < len(nums) - 1:
            end_pointer += 1
            if nums[end_pointer] != nums[start_pointer]:
                start_pointer += 1
                nums[start_pointer] = nums[end_pointer]
            else:
                if nums[start_pointer - 1] != nums[start_pointer]:
                    start_pointer += 1
                    nums[start_pointer] = nums[end_pointer]
        return start_pointer + 1


def main():
    answer = Solution()
    assert answer.removeDuplicates([1, 1, 1, 2, 2, 3]) == 5
    assert answer.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]) == 7
    print("All test cases passed.")


if __name__ == "__main__":
    main()
