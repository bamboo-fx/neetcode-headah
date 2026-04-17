class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        We're still just binary search and cutting data in half every time
        but instead this time what we have to do is we check if its target,
        ok now for mid when we compare, if mid is less than target what 
        does that mean, that means that the target is bigger than mid so its
        on the right side right so we should shift

        The thing is if mid is less than or greater than target that
        doesnt mean anything, you still dont know if its to the left or to
        the right, i think maybe the strat is still binary search where we are
        splitting an array in half every time, 
        """

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l+r) // 2

            # l = mid + 1
            if nums[mid] > nums[r]:
                l = mid + 1
                while l < r:
                    # normal binary search
                    middle = (l+r) // 2
                    if nums[middle] < target:
                        l = middle + 1
                    elif nums[middle] > target:
                        r = mid - 1
                    else:
                        return middle
            
            else:
                r = mid
                while l < r:
                    # normal binary search
                    middle = (l+r) // 2
                    if nums[middle] < target:
                        l = middle + 1
                    elif nums[middle] > target:
                        r = mid - 1
                    else:
                        return middle

        return -1