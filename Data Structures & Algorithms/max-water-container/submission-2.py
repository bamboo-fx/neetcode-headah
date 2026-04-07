class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Max is given by (r - l) * min(heights[l], heights[r]), and how to increment?
        The core logic is really how to increment?
        we should increment r no matter what, and when we reach something bigger
        than max we update max, otherwise we increment l
        """

        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            max_area = max(max_area, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area

