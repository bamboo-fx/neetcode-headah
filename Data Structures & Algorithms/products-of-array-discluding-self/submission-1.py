class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # form array to the left of a number
        # form array to the right of a number non inclusive
        # multiply left and right
        res = []
        for i in range(len(nums)):
            ans = 1
            left = nums[:i]
            right = nums[i+1:]
            for j in range(len(left)):
                ans *= left[j]
            for k in range(len(right)):
                ans *= right[k]
            res.append(ans)

        return res
