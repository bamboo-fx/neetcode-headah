class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        l = 0
        count = 0
        max_count = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.append(s[r])
            max_count = max(max_count, len(seen))

        return max_count