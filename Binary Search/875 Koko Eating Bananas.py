import math


class Solution:
    def get_total_time(self, piles: list[int], speed: int) -> int:
        return sum(math.ceil(pile / speed) for pile in piles)

    def find_upper_bound(self, max_speed: int, target: int, piles: list[int]) -> int:
        left, right = 1, max_speed
        answer = 1
        while left <= right:
            middle = (left + right) // 2
            total_time = self.get_total_time(piles, middle)
            if total_time <= target:
                answer = middle
                right = middle - 1
            else:
                left = middle + 1
        return answer

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        max_speed = max(piles)
        return self.find_upper_bound(max_speed, h, piles)


def main():
    ans = Solution()
    assert (output := ans.minEatingSpeed([3, 6, 7, 11], 8)) == 4, output
    assert (output := ans.minEatingSpeed([30, 11, 23, 4, 20], 5)) == 30, output
    assert (output := ans.minEatingSpeed([30, 11, 23, 4, 20], 6)) == 23, output

    print("Passed all tests!")


if __name__ == "__main__":
    main()
