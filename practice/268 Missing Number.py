class Solution:
    # def missingNumber(self, nums: list[int]) -> int:
    #     seen = set(nums)
    #     for i in range(len(nums) + 1):
    #         if i not in seen:
    #             return i
    #     return -1

    # Not using extra space
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
def main():
    answer = Solution()
    assert (output := answer.missingNumber([3, 0, 1])) == 2, f"output: {output}"
    assert (output := answer.missingNumber([0, 1])) == 2, f"output: {output}"
    assert (output := answer.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])) == 8, f"output: {output}"
    assert (output := answer.missingNumber([0])) == 1, f"output: {output}"

    print("Passed all test cases!")

if __name__ == '__main__':
    main()