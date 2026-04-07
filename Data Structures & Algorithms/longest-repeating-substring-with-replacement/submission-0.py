class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # dynamic sliding window with leading and lagging pointers

        # hashmap data structure
        # dynamic sliding window, frequency of each string,
        # logic for window size - max frequency has to less than k for replacements
        # finding the max res at every iteration

        freq = {}
        # key: character, value: frequency

        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)

            maxf = max(freq[s[r]], maxf)
            while (r - l + 1) - maxf > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

