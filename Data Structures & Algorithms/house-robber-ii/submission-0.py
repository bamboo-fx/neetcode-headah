class Solution:
    def rob(self, nums: List[int]) -> int:
        # bottom up

        if len(nums) == 0:
            return 0

        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
    def helper(self, nums):
        n = len(nums)
        dp = [0] * n
        dp[1] = nums[0]
        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return dp[-1]