class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1

def main():
    ans = Solution()
    assert (output := ans.search([-1, 0, 3, 5, 9, 12], 9)) == 4, output
    assert (output := ans.search([-1, 0, 3, 5, 9, 12], 2)) == -1, output
    assert (output := ans.search([5], 5)) == 0, output
    assert (output := ans.search([5], -5)) == -1, output

    print("Passed all tests!")

if __name__ == "__main__":
    main()