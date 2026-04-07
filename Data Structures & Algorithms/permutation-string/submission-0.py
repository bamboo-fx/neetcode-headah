class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        So basically just see if the characters in s1 are in s2.
        I think the strat is hashmap and sliding window
        """
        # base case
        if len(s2) < len(s1):
            return False
        
        l = 0
        tracker = {}
        for i in range(len(s1)):
            tracker[s1[i]] = 1 + tracker.get(s1[i], 0)
        
        window = {}
        for r in range(len(s2)):
            window[s2[r]] = 1 + window.get(s2[r], 0)

            if r - l + 1 > len(s1):
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    window.pop(s2[l])
                l += 1

            if window == tracker:
                return True

        return False

            
            
