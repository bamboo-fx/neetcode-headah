class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Ok so the approach is we iterate through nums keeping track with a score,
        for every element in nums we add to our score, once we reach target, we log
        elements that contributed to score, then we increment left pointer until
        less than score again, continuously do this and return the min, if we never
        hit target return 0

        I think we need a dictionary, the key should be score, and value should
        be constantly updated with the newest array if its a new minimum
        """

        score = 0
        l = 0
        result = []
        min_res = float('inf')
        for r in range(len(nums)):
            score += nums[r]
            while score >= target:
                min_res = min(min_res, r - l + 1)
                score -= nums[l]
                l += 1

        return 0 if min_res == float('inf') else min_res