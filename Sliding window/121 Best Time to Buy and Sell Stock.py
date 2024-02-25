class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = right = 0
        max_profit = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                max_profit = max(max_profit, prices[right] - prices[left])
            else:
                left = right
            right += 1

        return max_profit

def main():
    answer = Solution()
    assert (output := answer.maxProfit([7, 1, 5, 3, 6, 4])) == 5, f"output: {output}"
    assert (output := answer.maxProfit([7, 6, 4, 3, 1])) == 0, f"output: {output}"

    print("All tests passed!")

if __name__ == "__main__":
    main()