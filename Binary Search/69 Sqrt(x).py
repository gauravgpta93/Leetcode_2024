class Solution:
    def check_lower_multiple(self, x: int, mid: int) -> bool:
        return mid * mid <= x

    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left < right:
            mid = (left + right) // 2
            if self.check_lower_multiple(x, mid):
                left = mid + 1
            else:
                right = mid
        return left - 1 if left > 1 else left


def main():
    answer = Solution()
    assert (output := answer.mySqrt(4)) == 2, f"output: {output}"
    assert (output := answer.mySqrt(8)) == 2, f"output: {output}"
    assert (output := answer.mySqrt(1)) == 1, f"output: {output}"
    assert (output := answer.mySqrt(0)) == 0, f"output: {output}"
    assert (output := answer.mySqrt(2)) == 1, f"output: {output}"

    print("Passed all test cases!")


if __name__ == '__main__':
    main()
