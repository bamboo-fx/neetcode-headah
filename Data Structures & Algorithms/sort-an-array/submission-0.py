class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # recursively split the lists down in two
        def sortArray(nums):
            if len(nums) <= 1:
                return nums
            
            middle = len(nums) // 2
            left = self.sortArray(nums[:middle])
            right = self.sortArray(nums[middle:])

            return merge(left, right)

        # merge them

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

            result.extend(left[i:])
            result.extend(right[j:])
            return result

        nums[:] = sortArray(nums)
        return nums