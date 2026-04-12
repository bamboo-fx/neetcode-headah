class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # hashmap, key: number, value: frequency
        # order by frequency
        # if frequency >= n/3:
        # res.append(number)

        res = []
        tracker = {}
        n = len(nums)
        for i in range(len(nums)):
            tracker[nums[i]] = 1 + tracker.get(nums[i], 0)
        
        for (number, frequency) in tracker.items():
            if frequency > n/3:
                res.append(number)

        return res