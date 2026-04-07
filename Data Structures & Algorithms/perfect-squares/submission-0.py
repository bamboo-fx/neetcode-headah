class Solution:
    def numSquares(self, n: int) -> int:
        # min number

        dp = [n] * (n+1)
        # base case
        dp[0] = 0

        """
        so the end index will just be our integer n, and it will contain
        the number of perfect square that sum to n, that means each subamount
        will contain number of perfect squares that sub to subamount
        """
        # min number of perfect squares that sum to n
        for number in range(1, n+1):
            for s in range(1, number+1):
                square = s * s
                if number - square >= 0:
                    dp[number] = min(dp[number], 1 + dp[number-square])

        return dp[n]