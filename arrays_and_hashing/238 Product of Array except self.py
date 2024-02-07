class Solution:
    #     Solution 1: using two arrays
    #     def create_multiplication_array(self, nums: list[int], reverse: bool) -> list[int]:
    #         nums = nums[::-1] if reverse else nums
    #         result = []
    #         for num in nums:
    #             if not result:
    #                 result.append(num)
    #             else:
    #                 result.append(result[-1] * num)
    #         return result[::-1] if reverse else result
    #
    #     def productExceptSelf(self, nums: list[int]) -> list[int]:
    #         prefix_multiplication = self.create_multiplication_array(nums, False)
    #         suffix_multiplication = self.create_multiplication_array(nums, True)
    #         result = []
    #         for index in range(len(nums)):
    #             prefix = prefix_multiplication[index - 1] if index > 0 else 1
    #             suffix = suffix_multiplication[index + 1] if index < len(nums) - 1 else 1
    #             result.append(prefix * suffix)
    #         return result
    # def create_multiplication_array(self, org: list[int], result: list[int]) -> list[int]:
    #     for index in range(len(org) - 1):
    #         result[index + 1] = result[index] * org[index]
    #     return result

    def create_multiplication_array(self, org: list[int], result: list[int]) -> list[int]:
        product_value = 1
        for index in range(len(org)):
            result[index] *= product_value
            product_value *= org[index]
        return result

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)
        result = self.create_multiplication_array(nums, result)
        result = self.create_multiplication_array(nums[::-1], result[::-1])[::-1]
        # go backwards and multiply the current multiplication (of org)
        # current_multiplication = 1
        # for index in range(len(nums) - 1, -1, -1):
        #     result[index] *= current_multiplication
        #     current_multiplication *= nums[index]
        return result


def main():
    solution = Solution()
    assert solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert solution.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert solution.productExceptSelf([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert solution.productExceptSelf([]) == []
    print("All the test cases passed!")


if __name__ == "__main__":
    main()
