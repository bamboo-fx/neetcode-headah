class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        """
        right another sliding window problem but here we have a window of size k
        and we want to keep track of min difference between highest and lowest score
        
        So for this question since they dont have to be next to each other,
        the approach has to be like, hm maybe sort, then iterate through groups of k
        
        The sliding window approach has to be like, we always maintain a window
        of size k, within the window we must maintain the highest and lowest,
        and always compute difference and log min difference, my only issue is
        without a map how to keep track of which one is removed because we need to
        reset highest and lowest
        """

        nums.sort()

        l, r = 0, k - 1
        min_lowest = float('inf')
        while r < len(nums):
            min_lowest = min(min_lowest, nums[r] - nums[l])
            r += 1
            l += 1
        return min_lowest