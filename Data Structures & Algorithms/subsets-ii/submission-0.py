class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtracking(i, curr):
            if i == len(nums):
                res.append(curr.copy())
                return

            if i > len(nums):
                return
            
            curr.append(nums[i])
            backtracking(i + 1, curr)
            curr.pop()
            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            backtracking(i + 1, curr)

        backtracking(0, [])
        return res