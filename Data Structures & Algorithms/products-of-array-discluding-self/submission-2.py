class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # form array to the left of a number
        # form array to the right of a number non inclusive
        # multiply left and right
        
        # linear non space optimal
        # create prefix, suffix, results
        # calculate prefix and suffix, iterate through results and
        # add prefix * suffix

        # algorithm for prefix: prefix[i] = prefix[i-1] * nums[i-1]

        prefix = len(nums) * [0]
        suffix = len(nums) * [0]
        result = len(nums) * [0]

        prefix[0] = 1
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]

        suffix[len(nums)-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        for i in range(len(result)):
            result[i] = prefix[i] * suffix[i]

        return result