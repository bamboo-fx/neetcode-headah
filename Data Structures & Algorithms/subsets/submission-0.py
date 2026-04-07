class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        ah so basically backtracking right but we are having an array to store.

        in terms of parameters, we pass in index and empty subset.

        And then actual recursive call and backtracking oh and also conditional if
        base case

        basically yea just go through each index either include or don't
        """

        res = []
        def backtracking(i, curr):
            if i == len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            backtracking(i + 1, curr)
            curr.pop()

            backtracking(i + 1, curr)

        backtracking(0, [])
        return res
        