class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # order matters
        l = 0
        for r in range(len(t)):
            if t[r] == s[l]:
                l += 1

        return l == len(s)