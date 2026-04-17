class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        all = set(t)

        for i in range(len(s)):
            if s[i] not in all:
                return False

        return True