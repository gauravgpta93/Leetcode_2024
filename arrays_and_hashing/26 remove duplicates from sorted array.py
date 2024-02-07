class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        unique_val_pointer = 0
        current_pointer = 1
        while current_pointer < len(nums):
            if nums[unique_val_pointer] != nums[current_pointer]:
                unique_val_pointer += 1
                nums[unique_val_pointer] = nums[current_pointer]
            current_pointer += 1

        return unique_val_pointer + 1


def main():
    assert Solution().removeDuplicates([]) == 0
    assert Solution().removeDuplicates([1, 1, 2, 2, 3, 3, 4, 4]) == 4
    assert Solution().removeDuplicates([1, 1, 2]) == 2
    assert Solution().removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
    print('All test cases passed!')


if __name__ == '__main__':
    main()
