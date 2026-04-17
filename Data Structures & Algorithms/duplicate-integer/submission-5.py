class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = nums.set()
        for num in nums:
            if num in hashset:
                return True
        return False