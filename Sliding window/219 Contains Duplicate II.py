class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hash: dict[int, int] = {}
        for index, number in enumerate(nums):
            if number in hash and index - hash[number] <= k:
                return True
            hash[number] = index
        return False


def main():
    answer = Solution()
    assert (
        output := answer.containsNearbyDuplicate([1, 2, 3, 1], 3)
    ) is True, f"output: {output}"
    assert (
        output := answer.containsNearbyDuplicate([1, 0, 1, 1], 1)
    ) is True, f"output: {output}"
    assert (
        output := answer.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
    ) is False, f"output: {output}"

    print("All tests passed!")


if __name__ == "__main__":
    main()
