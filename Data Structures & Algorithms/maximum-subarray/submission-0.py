class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # brute force it, start for every i, then loop every possible j combination
        max_total = float('-inf')
        for i in range(len(nums)):
            cur = 0
            for j in range(i, len(nums)):
                cur += nums[j]
                max_total = max(max_total, cur)

        return max_total