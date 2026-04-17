class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set(nums)
        for num in nums:
            if num in hashset:
                return True
        return False