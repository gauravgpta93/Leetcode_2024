class Solution:
    # Modifing the array
    # def findDuplicate(self, nums: list[int]) -> int:
    #     for num in nums:
    #         if nums[abs(num) - 1] < 0:
    #             return abs(num)
    #         nums[abs(num) - 1] *= -1
    #     return -1

    # Without modifying the array
    def findDuplicate(self, nums: list[int]) -> int:
        if not nums:
            return -1
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # Another way can be finding the loop size and then go forward by n
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow


def main():
    ans = Solution()
    assert (output := ans.findDuplicate([1, 3, 4, 2, 2])) == 2, output
    assert (output := ans.findDuplicate([3, 1, 3, 4, 2])) == 3, output
    assert (output := ans.findDuplicate([1, 1])) == 1, output
    assert (output := ans.findDuplicate([1, 1, 2, 1])) == 1, output
    assert (output := ans.findDuplicate([2, 5, 9, 6, 9, 3, 8, 9, 7, 1])) == 9, output

    print("Passed all test cases!")


if __name__ == "__main__":
    main()
