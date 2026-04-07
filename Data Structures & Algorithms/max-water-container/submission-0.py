class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        i,j = 0, len(heights) - 1
        while i < j:
            area = min(heights[i],heights[j]) * (j-i)
            max_water = max(area, max_water)
            if heights[i] > heights[j]:
                j -=1
            else:
                i += 1
        return max_water