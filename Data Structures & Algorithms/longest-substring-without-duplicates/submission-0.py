class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # dynamic sliding window
        # string data structure
        # lag/lead
        seen = set()
        l = 0
        max_window = 0
        for r in range(1, len(s)):
            if s[r] in seen:
                l += 1
            seen.add(s[r])
            window = r - l
            max_window = max(max_window, window)
        return max_window