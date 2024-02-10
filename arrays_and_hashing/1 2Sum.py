# two sum

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lookup_index_table: dict[int, int] = {}
        for index, number in enumerate(nums):
            lookup_number = target - number
            lookup_number_index = lookup_index_table.get(lookup_number)
            if lookup_number_index is not None:
                return [lookup_number_index, index]
            lookup_index_table[number] = index
        return [-1, -1]  # This line will never be executed

def main():
    answer = Solution()
    assert answer.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert answer.twoSum([3, 2, 4], 6) == [1, 2]
    assert answer.twoSum([3, 3], 6) == [0, 1]
    assert answer.twoSum([3, 3], 7) == [-1, -1]
    print('All test cases passed.')


if __name__ == '__main__':
    main()
