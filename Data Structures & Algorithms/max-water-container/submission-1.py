class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Max is given by (r - l) * min(heights[l], heights[r]), and how to increment?
        The core logic is really how to increment?
        we should increment r no matter what, and when we reach something bigger
        than max we update max, otherwise we increment l
        """

        l = 0
        max_area = 0
        for r in range(1, len(heights)):
            new_area = (r - l) * min(heights[l], heights[r])
            if max_area < new_area:
                max_area = new_area
            if heights[r] > heights[l]:
                l = r
        
        return max_area


