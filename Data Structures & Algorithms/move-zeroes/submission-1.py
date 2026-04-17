class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                while nums[l] != 0 and l < len(nums):
                    l += 1
                nums[l] = nums[r]
                nums[r] = 0

