class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # dynamic sliding window
        # string data structure
        # lag/lead
        seen = set()
        l = 0
        max_window = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            window = r - l + 1
            max_window = max(max_window, window)
        return max_window