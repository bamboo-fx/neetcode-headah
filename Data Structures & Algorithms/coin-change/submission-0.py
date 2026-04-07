class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # what kind of dynammic programming is this question?

        """
        Ok so it seems that the core logic is as follows: given our coins list,
        we are going to create an array dp, where at each index we put the
        min number of coins to add up to that min target index amount, then
        to reach final amount we build off all the previous i guess? still a bit
        confused but ill try to write it out rn
        """
        
        
        
        """
        Ok here is the algorithm: initialize an array with subamounts, length 0
        all the way until our actual amount, each index contains the number of coins to
        get to that subamount, start with base case 0 coins for 0 amount. then we build
        iteratively, loop through every subamount, for every subamount we loop through trying
        all of our coins, for a given coin if its less than amount, we can then then update
        the coins needed to make that subamount by adding our 1 coin + the minimum needed to get 
        the subamount minus that coin, the amount of coins, we protect against not perfectly sum
        by essentially what we do is we have to call dp[a-c], this means there must be a sum, if there
        is not then we just end up skipping over with dp[a-c], because if previous cannot be
        perfectly made then it ends up being the defaulted amount+1, at the very end we just return
        the subamount at index amount if its not equal to amount+1 otherwise return -1
        """
        # goal: using coins find min number to sum to amount

        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a-c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        
        return dp[amount] if dp[amount] != amount+1 else -1



