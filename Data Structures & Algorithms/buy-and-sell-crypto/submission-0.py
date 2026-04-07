class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        # two pointers, fast and slow
        i, j = 0, 1
        while j < len(prices):
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]
                max_profit = max(profit, max_profit)
            else:
                i = j
            j += 1
        return max_profit
