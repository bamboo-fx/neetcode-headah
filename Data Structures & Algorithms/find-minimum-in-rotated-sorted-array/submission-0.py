class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Literally search the array by getting rid of half at a time, literally
        slicing at midpoint everytime. If the mid is greater than the left, 
        that means that we are still increasing so that means min is to
        the right of mid. if mid is less than left that means we are decreasing
        so that means min is on the left. if mid is equal to left
        """

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            # smallest is to the right
            if nums[mid] >= nums[l]:
                l = mid + 1
            # 
            else:
                r = mid

        return nums[l]