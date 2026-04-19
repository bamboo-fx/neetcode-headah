class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # if window length - most frequent <= k
        l = 0
        frequency = {}
        max_len = 0
        for r in range(len(s)):
            frequency[s[r]] = 1 + frequency.get(s[r], 0)
            while l < len(s) and (r - l + 1) - max(frequency.values()) > k:
                frequency[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len