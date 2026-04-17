class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1] * len(text2) for _ in range(len(text1))]
        def dfs(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0

            if text1[i] == text2[j]:
                return 1 + max(dfs(i+1, j), dfs(i, j+1))

            if text1[i] != text2[j]:
                return 0 + max(dfs(i+1, j), dfs(i, j+1))

            if memo[i][j] != -1:
                return memo[i][j]

            memo[i][j] = memo[i-1][j-1] + max(dfs(i+1, j), dfs(i, j+1))
            return memo        
        return dfs(0,0)

            