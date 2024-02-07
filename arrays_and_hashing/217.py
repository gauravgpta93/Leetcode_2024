# Find if the array contains atleast one element with which occurs twice
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        already_seen: set[int] = set()
        for num in nums:
            if num in already_seen:
                return True
            already_seen.add(num)
        return False


def main():
    answer = Solution()
    assert answer.containsDuplicate([]) is False
    assert answer.containsDuplicate([1, 2, 3, 1])
    assert answer.containsDuplicate([1, 2, 3, 4]) is False
    assert answer.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
    print('All test cases passed.')


if __name__ == '__main__':
    main()
