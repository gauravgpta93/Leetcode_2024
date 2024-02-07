class Solution:
    # def removeElement(self, nums: list[int], val: int) -> int:
    #     result_pointer: int = -1
    #     for value in nums:
    #         if value != val:
    #             result_pointer += 1
    #             nums[result_pointer] = value
    #     return result_pointer + 1

    # Can also use list slicing to do in-place removal of elements
    def removeElement(self, nums: list[int], val: int) -> int:
        nums[:] = [i for i in nums if i != val]
        return len(nums)

def main():
    assert Solution().removeElement([], 0) == 0
    assert Solution().removeElement([3, 2, 2, 3], 3) == 2
    assert Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
    assert Solution().removeElement([1], 1) == 0
    assert Solution().removeElement([1, 1, 1, 1], 1) == 0
    print('All test cases passed!')


if __name__ == '__main__':
    main()
