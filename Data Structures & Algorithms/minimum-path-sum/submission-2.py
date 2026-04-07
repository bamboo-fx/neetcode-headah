class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:        
        m = len(grid)
        n = len(grid[0])
        memo = [[-1] * n for _ in range(m)]

        def dfs(down, right):
            if down >= m or right >= n:
                return float('inf')
            
            if down == m-1 and right == n-1:
                return grid[m-1][n-1]

            if memo[down][right] != -1:
                return memo[down][right]

            memo[down][right] = grid[down][right] + min(dfs(down+1, right), dfs(down, right+1))
            return memo[down][right]
        
        return dfs(0,0)