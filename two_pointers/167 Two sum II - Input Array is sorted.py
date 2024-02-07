class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        start_pointer, end_pointer = 0, len(numbers) - 1
        while start_pointer < end_pointer:
            sum = numbers[start_pointer] + numbers[end_pointer]
            if sum == target:
                return [start_pointer + 1, end_pointer + 1]
            elif sum < target:
                start_pointer += 1
            else:
                end_pointer -= 1
        return [-1, -1]

def main():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert Solution().twoSum([2, 3, 4], 6) == [1, 3]
    assert Solution().twoSum([-1, 0], -1) == [1, 2]
    print('All test cases passed!')


if __name__ == "__main__":
    main()
