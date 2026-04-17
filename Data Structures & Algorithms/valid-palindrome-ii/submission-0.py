class Solution:
    def validPalindrome(self, s: str) -> bool:
        # data structure, string
        # algorithm, two pointers at the end

        # trick,

        # normal:
        counter = 1
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                counter -= 1
            if counter < 0:
                return False
            i += 1
            j -= 1

        return True