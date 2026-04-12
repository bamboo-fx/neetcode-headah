class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # data structure, array, hashset

        if len(nums) == 0:
                return 0
    
        nums.sort()
        total = 1
        max_total = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                total += 1
            elif nums[i] == nums[i-1]:
                continue
            elif nums[i] != nums[i-1] + 1:
                total = 1
            max_total = max(total, max_total)

        return max_total