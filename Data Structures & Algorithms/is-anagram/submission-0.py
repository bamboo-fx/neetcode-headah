class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagrams if all same characters, and all same frequency
        # if strings are different length return false
        if len(s) != len(t):
            return False
        # create two empty dictionarys
        countt, counts = {}, {}
        # collect the frequency
        for i in range(len(t)):
            countt[t[i]] = 1 + countt.get(t[i],0)
            counts[s[i]] = 1 + counts.get(s[i],0)
        return countt == counts

        