from collections import defaultdict, Counter


class Solution:
    # This uses sorting
    # def create_result(self, top_k: int, count_numbers: dict[int, list[int]]) -> list[int]:
    #     result = []
    #     current_count = 0
    #     sorted_count_numbers = sorted(count_numbers.items(), reverse=True)
    #     for count, numbers in sorted_count_numbers:
    #         for number in numbers:
    #             if current_count >= top_k:
    #                 return result
    #             result.append(number)
    #             current_count += 1
    #     return result

    # This uses manually going through the dictionary
    def create_result(self, top_k: int, count_numbers: dict[int, list[int]]) -> list[int]:
        result = []
        current_count = 0
        total_count = sum(count_numbers.keys())
        for count in range(total_count, 0, -1):
            if count not in count_numbers:
                continue
            for number in count_numbers[count]:
                if current_count >= top_k:
                    return result
                result.append(number)
                current_count += 1
        return result

    def get_count_numbers(self, number_count: dict[int, int]) -> dict[int, list[int]]:
        count_numbers: dict[int, list[int]] = defaultdict(list)
        for number, count in number_count.items():
            count_numbers[count].append(number)

        return count_numbers

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        number_count = Counter(nums)
        count_numbers = self.get_count_numbers(number_count)
        return self.create_result(k, count_numbers)


def main():
    answer = Solution()
    assert answer.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2) == [-1, 2]
    assert answer.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    assert answer.topKFrequent([1], 1) == [1]
    assert answer.topKFrequent([1, 2], 2) == [1, 2]
    print('All test cases passed.')


if __name__ == '__main__':
    main()
