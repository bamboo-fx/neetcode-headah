class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # you are always going down or right, so every state you have two decisions
        # you either go down or you go up

        # memo
        memo = [[-1] * n for _ in range(m)]
        def dfs(row, col):
            # base case:
            if row == m-1 and col == n-1:
                return 1

            elif row >= m or col >= n:
                return 0

            elif memo[row][col] != -1:
                return memo[row][col]

            memo[row][col] = dfs(row+1, col) + dfs(row, col+1)
            return memo[row][col]
        
        return dfs(0,0)


            
