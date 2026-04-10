class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # space optimal
        # forward pass then backward pass
        # key trick is to not generate new arrays for forward and backward
        # key idea is go from left to right first, calculate all elements multiplied
        # to the left of the array
        # multiply that with value to the right working backwards

        res = len(nums) * [0]

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res