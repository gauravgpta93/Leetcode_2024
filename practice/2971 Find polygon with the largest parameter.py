class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()
        sum_list = []
        current_sum = 0
        for num in nums:
            current_sum += num
            sum_list.append(current_sum)
        for index in range(len(nums) -1, 1, -1):
            if nums[index] < sum_list[index-1]:
                return sum_list[index]
        return -1



def main():
    ans = Solution()
    assert ans.largestPerimeter([2, 1, 2]) == 5
    assert ans.largestPerimeter([1, 2, 1]) == -1
    assert ans.largestPerimeter([5, 5, 5]) == 15
    assert (result := ans.largestPerimeter([1, 12, 1, 2, 5, 50, 3])) == 12, f"Test case failed: {result}"
    assert ans.largestPerimeter([5, 5, 50]) == -1


if __name__ == '__main__':
    main()
