class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # two pointers at the end
        # consistently find midpoint and shift
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low+high)//2
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                return mid
        return -1