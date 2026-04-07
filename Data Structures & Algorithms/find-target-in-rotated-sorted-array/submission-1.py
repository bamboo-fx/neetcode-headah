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
        splitting an array in half every time

        Got it, so heres what we do, find min, this splits the array in half, define smaller
        binary search, perform on both sides and return -1 or number if found

        """

        l, r = 0, len(nums) - 1

        while l < r:
            # normal binary search
            middle = (l+r) // 2
            if nums[middle] > nums[r]:
                l = middle + 1
            else:
                r = middle
        
        pivot = l

        def find_target(left, right):
            l = left
            r = right
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
            return -1

        result = find_target(0, pivot - 1)
        if result != -1:
            return result

        return find_target(pivot, len(nums)-1)
            