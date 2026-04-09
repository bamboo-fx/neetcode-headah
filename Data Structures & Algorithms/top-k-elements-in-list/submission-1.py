class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap to count the frequency, key: number, value: frequency
        # sort by frequency
        # reverse
        # top k

        tracker = {}
        for i in range(len(nums)):
            tracker[nums[i]] = 1 + tracker.get(nums[i], 0)

        arr = []
        for (number, frequency) in tracker.items():
            arr.append((frequency, number))

        arr.sort()
        arr.reverse()
        answer = []
        # how to get the numbers only now?
        for frequency, number in arr:
            answer.append(number)

        return answer[:k]
