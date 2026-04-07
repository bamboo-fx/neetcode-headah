class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousnum = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in previousnum:
                return [previousnum[needed], i]
            else:
                previousnum[nums[i]] = i