class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # pretty simple int array
        # algorithm is just two pointers but within 2 for loops basically with some checks


        nums.sort()
        ans = []


        # basically a check where i is held constant, j is one after and held constant,
        # then we just two pointer logic the rest, continue if duplicates, start when
        # i and j have previous to compare with, if condition not met go into the while 
        # loop
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                l, r = j + 1, len(nums) - 1
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total == target:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif total < target:
                        l += 1
                    else:
                        r -= 1
        return ans
                    