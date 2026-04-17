class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # recursively break down into subproblems
        # difference is that if we encounter ever that one of the given
        # i j is equal to 1 then we return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = [[0] * n for _ in range(m)]
        def dfs(row, col):
            # base case:
            if row >= m or col >= n:
                return 0
            if obstacleGrid[row][col] == 1:
                return 0
            if row == m-1 and col == n-1:
                return 1

            if memo[row][col] != obstacleGrid[row][col]:
                memo[row][col] = obstacleGrid[row][col]
            # new case where we hit an obstacle
            return dfs(row+1, col) + dfs(row, col+1)
        return dfs(0,0)

        # I really think here the difference is that if we hit a point which contains 1
        # then that means what, if we hit a point that is 1 then that means that its a deadend essentially
        # so basically if we hit 1, that path should just return 0