class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap, key: number, value: frequency
        # sort by frequency, reverse, choose the top k


        tracker = {}
        for i in range(len(nums)):
            tracker[nums[i]] = 1 + tracker.get(nums[i], 0)


        res = []
        # get the dictionary instead into a list where they we sort
        # something like list of (frequency, number)

        for (number, frequency) in tracker.items():
            res.append((frequency, number))

        res.sort()

        res.reverse()

        new = []
        for i, (freq, num) in enumerate(res):
            new.append(num)

        return new[:k]


