class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # bottom up tabulation
        dp = [*nums]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])

        return max(dp)