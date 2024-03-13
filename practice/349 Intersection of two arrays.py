from collections import Counter


class Solution:
    # def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
    #     counter_1: dict[int, int] = Counter(nums1)
    #     counter_2: dict[int, int] = Counter(nums2)
    #     result_hash: dict[int, int] = {}
    #     for key in counter_1:
    #         result_hash[key] = min(counter_1[key], counter_2.get(key, 0))
    #     # print(result_hash)
    #     return [value for value, count in result_hash.items() if count != 0]

    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))

def main():
    solution = Solution()
    assert (result := solution.intersection([1, 2, 2, 1], [2, 2])) == [2], f"unexpected {result=}"
    assert (result := solution.intersection([4, 9, 5], [9, 4, 9, 8, 4])) == [4, 9], f"unexpected {result=}"


if __name__ == "__main__":
    main()
