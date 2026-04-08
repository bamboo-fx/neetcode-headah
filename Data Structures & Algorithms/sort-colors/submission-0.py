class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def sortArray(nums):
            # base case
            if len(nums) == 1:
                return nums
            
            middle = len(nums) // 2
            left = sortArray(nums[:middle])
            right = sortArray(nums[middle:])

            return merge(left, right)


        def merge(left, right):
            result = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            while i < len(left):
                result.append(left[i])
                i += 1
            while j < len(right):
                result.append(right[j])
                j += 1

            return result

        nums[:] = sortArray(nums)