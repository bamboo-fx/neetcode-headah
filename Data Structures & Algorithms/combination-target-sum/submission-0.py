class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Never really done a backtracking problem before so honestly idek lmao,
        but apparently its like dfs, if its like dfs, then what does that mean?
        It has a stack, internal or external, 
        """
        res = []

        def backtracking(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or total > target:
                return

            curr.append(nums[i])
            backtracking(i, curr, total + nums[i])
            curr.pop()
            backtracking(i + 1, curr, total)

        backtracking(0, [], 0)
        return res
