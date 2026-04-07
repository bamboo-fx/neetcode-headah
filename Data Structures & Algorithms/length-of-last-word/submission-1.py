class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        reversed = s[::-1]
        for i in range(len(reversed)):
            if reversed[i] != " ":
                result += 1
            if result > 0 and reversed[i] == " ":
                return result

        return result