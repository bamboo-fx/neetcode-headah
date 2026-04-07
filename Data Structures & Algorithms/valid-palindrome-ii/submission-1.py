class Solution:
    def validPalindrome(self, s: str) -> bool:
        # data structure, string
        # algorithm, two pointers at the end

        # helper function
        # trick though is just know skip left or skip right

        # optimal with helper
        def isvalidPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return (isvalidPalindrome(l+1, r) or isvalidPalindrome(l, r-1))

            l += 1
            r -= 1
        return True