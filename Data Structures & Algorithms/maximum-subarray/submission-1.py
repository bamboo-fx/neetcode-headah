class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # recursion

        def dfs(i, flag):
            # base case, end of array return 0 if in continuous array or just don't be affected
            if i == len(nums):
                return 0 if flag else -100000
            # flag is true and we decide end or continue
            if flag:
                return max(0, nums[i] + dfs(i + 1, True))
            # flag is false and we decide here or skip
            return max(dfs(i + 1, False), nums[i] + dfs(i + 1, True))

        return dfs(0, False)