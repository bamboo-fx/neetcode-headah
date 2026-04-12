class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # data structure, array, hashset

        # if nums[i] - 1 not in set, that number is minimum
        # if nums[i] - 1 in set: total += 1

        seen = set(nums)
        
        # if nums[i] - 1 not in seen, then thats the starting point
        # while that number is in seen, total += 1
        max_total = 0
        for number in seen:
            if number - 1 not in seen:
                total = 1
                while number + 1 in seen:
                    total += 1
                    number += 1
                max_total = max(max_total, total)

        return max_total
                    
            