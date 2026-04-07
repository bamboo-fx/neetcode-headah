class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # brute force
        max_total = float("-inf")
        for i in range(len(nums)):
            curr = 0
            for j in range(i, len(nums)):
                curr += nums[j]
                max_total = max(max_total, curr)
        return max_total
        