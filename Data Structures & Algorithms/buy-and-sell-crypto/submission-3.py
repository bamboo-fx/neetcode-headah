class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i,j = 0,1
        while j<len(prices):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
            else:
                i = j
            j += 1

        return max_profit


        
