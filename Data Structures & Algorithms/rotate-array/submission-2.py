class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # extra space linear
        # create a temp array
        # value at index in temp is just (i + k) % len(nums)
        # as in the value in the temp at i is just rotated by k
        # amount from original
        # then copy it into the original


        temp = [0] * len(nums)
        for i in range(len(nums)):
            temp[i] = nums[(i-k) % len(nums)]
        nums[:] = temp
        return nums