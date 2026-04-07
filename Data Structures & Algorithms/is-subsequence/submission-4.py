class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # order matters
        if not s:
            return True
        l = 0
        for r in range(len(t)):
            if t[r] == s[l]:
                l += 1
                if l == len(s):
                    return True
        return l == len(s)