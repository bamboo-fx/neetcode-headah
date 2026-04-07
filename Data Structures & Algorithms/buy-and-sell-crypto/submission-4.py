class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        i,j = 0,1
        while j < len(prices):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                maxp = max(profit, maxp)
            else:
                i = j
            j += 1
        return maxp


        
