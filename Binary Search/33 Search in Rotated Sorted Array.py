class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


def main():
    answer = Solution()
    assert (output := answer.search([4, 5, 6, 7, 0, 1, 2], 0)) == 4, f"output: {output}"
    assert (output := answer.search([4, 5, 6, 7, 0, 1, 2], 3)) == -1, f"output: {output}"
    assert (output := answer.search([1], 0)) == -1, f"output: {output}"
    assert (output := answer.search([1, 3, 5], 5)) == 2, f"output: {output}"

    print("Passed all test cases!")


if __name__ == '__main__':
    main()
