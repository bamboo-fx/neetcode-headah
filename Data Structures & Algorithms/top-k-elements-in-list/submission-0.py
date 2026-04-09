class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = {}
        for i in range(len(nums)):
            tracker[nums[i]] = 1 + tracker.get(nums[i], 0)
        # sort it by value
        arr = []
        for num, freq in tracker.items():
            arr.append((freq, num))

        arr.sort()

        ans = []
        for (answer, leave) in arr:
            ans.append(leave)
        ans.reverse()

        return ans[:k]