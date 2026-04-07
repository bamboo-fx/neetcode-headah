class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # recursion

        # dfs implemntation, decision tree, in array or not -> continue or not

        def dfs(i, flag):
            if i == len(nums):
                return 0 if flag else -1000000

            if flag:
                return max(0, nums[i] + dfs(i+1, True))

            # skip or keep
            return max(dfs(i+1, False), nums[i] + dfs(i+1, True))

        return dfs(0, False)