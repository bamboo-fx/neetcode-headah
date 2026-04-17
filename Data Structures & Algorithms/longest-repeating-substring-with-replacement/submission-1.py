class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """

        """

        
        frequency_mapping = {}
        for i in range(len(s)):
            frequency_mapping[s[i]] = 1 + count.get(s[i], 0)
            if window - max(frequency_mapping.value()) > k:
                l += 1

        return window