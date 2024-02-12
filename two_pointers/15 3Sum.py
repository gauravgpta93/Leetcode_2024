class Solution:
    # using a set to seen values.
    # def two_sum(self, nums: list[int], target: int) -> list[list[int]]:
    #     seen_count: set[int] = set()
    #     result: set[tuple[int, ...]] = set()
    #     for number in nums:
    #         lookup_number = target - number
    #         if lookup_number in seen_count:
    #             result.add(tuple(sorted([number, lookup_number])))
    #         seen_count.add(number)
    #     return [list(pair) for pair in result]
    #
    # def threeSum(self, nums: list[int]) -> list[list[int]]:
    #     result: set[tuple[int, ...]] = set()
    #     for start_index in range(0, len(nums) - 2, 1):
    #         target = -nums[start_index]
    #         two_sum_result = self.two_sum(nums[start_index + 1 :], target)
    #         for pair in two_sum_result:
    #             result.add(tuple(sorted([nums[start_index], *pair])))
    #     return [list(value) for value in result]

    # sorting and getting two sum from the remainder.
    # def threeSum(self, nums: list[int]) -> list[list[int]]:
    #     nums.sort()
    #     result: set[tuple[int, ...]] = set()
    #     for index, num in enumerate(nums):
    #         if num > 0:
    #             break
    #         target = -num
    #         start_index = index + 1
    #         end_index = len(nums) - 1
    #         while start_index < end_index:
    #             two_sum = nums[start_index] + nums[end_index]
    #             if two_sum == target:
    #                 result.add(tuple(sorted([num, nums[start_index], nums[end_index]])))
    #                 start_index += 1
    #                 end_index -= 1
    #             elif two_sum < target:
    #                 start_index += 1
    #             else:
    #                 end_index -= 1
    #     return [list(value) for value in result]

    def get_total_zero(
        self, pair_of_same_type: list[int], set_of_opp_type: set[int]
    ) -> set[tuple[int, ...]]:
        result: set[tuple[int, ...]] = set()
        for index, first_value in enumerate(pair_of_same_type):
            sub_list = pair_of_same_type[index + 1 :]
            for second_value in sub_list:
                total = first_value + second_value
                if -total in set_of_opp_type:
                    result.add(tuple(sorted([first_value, second_value, -total])))
        return result

    # using the property of 0 sum approach.
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        negative_list, positive_list, zero_count = [], [], 0
        negative_set, positive_set = set(), set()
        result: set[tuple[int, ...]] = set()
        for number in nums:
            if number < 0:
                negative_list.append(number)
                negative_set.add(number)
            elif number > 0:
                positive_list.append(number)
                positive_set.add(number)
            else:
                zero_count += 1
        if zero_count >= 3:
            result.add((0, 0, 0))
        if zero_count > 0:
            for number in positive_set:
                if -number in negative_set:
                    result.add(tuple([-number, 0, number]))
        result |= self.get_total_zero(negative_list, positive_set)
        result |= self.get_total_zero(positive_list, negative_set)
        return [list(value) for value in result]


def main():
    answer = Solution()
    assert answer.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert answer.threeSum([-1, 0, 1, 2, 2, -1, -4]) == [
        [-1, -1, 2],
        [-1, 0, 1],
        [-4, 2, 2],
    ]
    assert answer.threeSum([0, 0, 0]) == [[0, 0, 0]]
    assert answer.threeSum([]) == []
    assert answer.threeSum([0]) == []
    print("All test cases passed.")


if __name__ == "__main__":
    main()
