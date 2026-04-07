class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """

        """

        l, r = 0, 0
        frequency_mapping = {}
        max_window = 0
        for r in range(len(s)):
            frequency_mapping[s[r]] = 1 + frequency_mapping.get(s[r], 0)
            while (r-l+1) - max(frequency_mapping.values()) > k:
                frequency_mapping[s[l]] -= 1
                l += 1

            max_window = max(max_window, r-l+1)


        return max_window