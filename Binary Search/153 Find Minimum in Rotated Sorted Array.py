class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]
            middle = (right + left) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
        return nums[left]

def main():
    ans = Solution()
    assert (output := ans.findMin([3, 4, 5, 1, 2])) == 1, output
    assert (output := ans.findMin([4, 5, 6, 7, 0, 1, 2])) == 0, output
    assert (output := ans.findMin([4, 5, 6, 7, 0, 1, 2, 3])) == 0, output
    assert (output := ans.findMin([11, 13, 15, 17])) == 11, output
    assert (output := ans.findMin([2, 1])) == 1, output
    assert (output := ans.findMin([1])) == 1, output
    assert (output := ans.findMin([3, 1, 2])) == 1, output

    print("Passed all tests!")


if __name__ == "__main__":
    main()
