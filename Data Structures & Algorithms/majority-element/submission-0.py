class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mappers = {}
        for i in range(len(nums)):
            mappers[nums[i]] = 1 + mappers.get(nums[i], 0)

        return max(mappers.keys())