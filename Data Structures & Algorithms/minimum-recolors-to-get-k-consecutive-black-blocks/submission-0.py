class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """
        Ok so the way to approach this problem is that essentially we want a sliding
        window keeping track of like blacks and whites, number of whites needed
        to convert to black, and then also keeping track of window with the
        minimal number of conversions.

        Ok so the issue im running into is that I think what I need is to implement
        either a map or a set, i think its implement a map, and then anytime the window
        gets to big remove the left most element from set, and compare just value of W in map
        not a separate tracker element

        Ok so my new implementation right now right, i just iterate through, create
        my dictionary, and whenever our window is too long, we shall shrink it, then we decrement
        whatever the leftmost element happens to be, hmmm maybe its something thats wrong
        with the min_switch check, so right now im checking the min number of W's.

        Wait I have the logic wrong, its not the window length is k, its 
        """



        l = 0
        min_switch = float('inf')
        tracker = {}
        for r in range(len(blocks)):
            tracker[blocks[r]] = 1 + tracker.get(blocks[r],0)
            # whats the condition for shifting left pointer?
            if r - l + 1 > k:
                tracker[blocks[l]] -= 1
                l += 1
            if r - l + 1 == k:
                min_switch = min(min_switch, tracker.get('W', 0))
        return min_switch