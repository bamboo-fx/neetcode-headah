class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # the key idea is that we just keep a counter, every time its not
        # the majority we subtract, when we reach 0 we set the next one
        # as our new candidate since its the majority and will come out on top

        res = 0
        count = 0

        for num in nums:
            if count == 0:
                res = num
            count += (1 if res == num else -1)

        return res