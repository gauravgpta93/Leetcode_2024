from collections import defaultdict


class Solution:
    # def create_temp_indexes(self, temperatures: list[int]) -> dict[int, list[int]]:
    #     temp_indexes: dict[int, list[int]] = defaultdict(list)
    #     for index, temp in enumerate(temperatures):
    #         temp_indexes[temp].append(index)
    #     return temp_indexes
    #
    # def find_lowest_higher_temp_index(
    #     self, temp_indexes: dict[int, list[int]], temp: int
    # ) -> int:
    #     min_index: int | None = None
    #     for temperature, indexes in temp_indexes.items():
    #         if temperature > temp:
    #             min_index = min(min_index, indexes[0]) if min_index else indexes[0]
    #     return min_index if min_index is not None else 0
    #
    # def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
    #     result = []
    #     temp_indexes = self.create_temp_indexes(temperatures)
    #     for index, temp in enumerate(temperatures):
    #         min_index = self.find_lowest_higher_temp_index(temp_indexes, temp)
    #         result.append((min_index - index) if min_index else 0)
    #         temp_indexes[temp].pop(0)
    #         if not temp_indexes[temp]:
    #             del temp_indexes[temp]
    #     return result

    # Using Stack (backward iteration)
    # def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
    #     temperature_stack = []
    #     reverse_temperature = temperatures[::-1]
    #     result = []
    #     for index, temperature in enumerate(reverse_temperature):
    #         while temperature_stack and temperature >= temperature_stack[-1][0]:
    #             temperature_stack.pop()
    #         if temperature_stack:
    #             result.append(index - temperature_stack[-1][1])
    #         else:
    #             result.append(0)
    #         temperature_stack.append((temperature, index))
    #     return result[::-1]

    # Using Stack (forward iteration)
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        temperature_stack = []
        result = [0] * len(temperatures)
        for index, temperature in enumerate(temperatures):
            while temperature_stack and temperature > temperature_stack[-1][0]:
                prev_index = temperature_stack.pop()[1]
                result[prev_index] = index - prev_index
            temperature_stack.append((temperature, index))
        return result


def main():
    sol = Solution()
    assert (result := sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])) == [
        1,
        1,
        4,
        2,
        1,
        1,
        0,
        0,
    ], f"expected {result=}"
    assert (result := sol.dailyTemperatures([30, 40, 50, 60])) == [
        1,
        1,
        1,
        0,
    ], f"expected {result=}"
    assert (result := sol.dailyTemperatures([30, 60, 90])) == [
        1,
        1,
        0,
    ], f"expected {result=}"

    print("All test cases passed!")


if __name__ == "__main__":
    main()
