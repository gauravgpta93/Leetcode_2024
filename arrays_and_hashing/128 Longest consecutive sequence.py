class Solution:
    def get_max_consecutive_sequence(self, start: int, unique_vals: set[int]) -> int:
        count = 1
        current = start
        while current + 1 in unique_vals:
            count += 1
            current += 1
        return count

    def get_starting_values(self, unique_vals: set[int]) -> set[int]:
        starting_values = set()
        for val in unique_vals:
            if val - 1 not in unique_vals:
                starting_values.add(val)
        return starting_values

    def longestConsecutive(self, nums: list[int]) -> int:
        unique_vals = set(nums)
        max_count = 0
        starting_values = self.get_starting_values(unique_vals)
        for start in starting_values:
            max_count = max(max_count, self.get_max_consecutive_sequence(start, unique_vals))
        return max_count

def main():
    assert Solution().longestConsecutive([]) == 0
    assert Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert Solution().longestConsecutive([1, 2, 0, 1]) == 3
    assert Solution().longestConsecutive([1, 2, 0, 1, 2]) == 3
    assert Solution().longestConsecutive([1, 2, 0, 1, 2, 3]) == 4
    print('All test cases passed!')


if __name__ == '__main__':
    main()
