class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # start with i, j = 0, 1
        # area = min(heights[i], heights[j]) * (j-i+1)
        # max_area = max(max_area, area)
        # j += 1
        # brute force
        max_area = 0
        for i in range(len(heights)):
            j = i + 1
            while j < len(heights):
                area = min(heights[i], heights[j]) * (j-i)
                max_area = max(max_area, area)
                j += 1
        return max_area