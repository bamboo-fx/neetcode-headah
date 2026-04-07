class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = 0
        memo = [[-1] * n for _ in range(m)]
        def dfs(row, col):
            # base case
            if row >= m or col >= n:
                return float('inf')
            if row == m-1 and col == n-1:
                return grid[m-1][n-1]
            if memo[row][col] != -1:
                return memo[row][col]

            memo[row][col] = grid[row][col] + min(dfs(row+1, col), dfs(row, col+1))
            
            return memo[row][col]

        return dfs(0,0)